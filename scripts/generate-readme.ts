#!/usr/bin/env bun

type Project = {
  name: string;
  url: string;
  summary: string;
};

const dataPath = new URL("../data/featured_repos.json", import.meta.url);
const readmePath = new URL("../README.md", import.meta.url);
const readmeStart = "<!-- BEGIN GENERATED FEATURED REPOS -->";
const readmeEnd = "<!-- END GENERATED FEATURED REPOS -->";

function isProject(value: unknown): value is Project {
  if (!value || typeof value !== "object") {
    return false;
  }

  const candidate = value as Record<string, unknown>;
  return (
    typeof candidate.name === "string" &&
    typeof candidate.url === "string" &&
    typeof candidate.summary === "string"
  );
}

async function loadProjects(): Promise<Project[]> {
  const projects = await Bun.file(dataPath).json();

  if (!Array.isArray(projects)) {
    throw new Error("featured_repos.json must contain an array");
  }

  projects.forEach((project, index) => {
    if (!isProject(project)) {
      throw new Error(`Project #${index} must include string name, url, and summary fields`);
    }
  });

  return projects;
}

function formatProject(project: Project): string {
  return `- **[${project.name}](${project.url})** - ${project.summary}`;
}

function replaceManagedBlock(text: string, body: string): string {
  const startMarker = text.indexOf(readmeStart);
  const endMarker = text.indexOf(readmeEnd);

  if (startMarker === -1 || endMarker === -1 || endMarker < startMarker) {
    throw new Error("Missing README managed block markers");
  }

  const blockStart = startMarker + readmeStart.length;
  return `${text.slice(0, blockStart)}\n${body}\n${text.slice(endMarker)}`;
}

async function main(): Promise<void> {
  const check = Bun.argv.includes("--check");
  const [projects, currentReadme] = await Promise.all([
    loadProjects(),
    Bun.file(readmePath).text(),
  ]);
  const expectedReadme = replaceManagedBlock(
    currentReadme,
    projects.map(formatProject).join("\n"),
  );

  if (currentReadme === expectedReadme) {
    console.log("README.md: up to date");
    return;
  }

  if (check) {
    console.error("README.md: needs regeneration");
    process.exitCode = 1;
    return;
  }

  await Bun.write(readmePath, expectedReadme);
  console.log("README.md: regenerated");
}

await main();
