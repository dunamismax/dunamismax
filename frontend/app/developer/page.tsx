export default function DeveloperPage() {
  const projects = [
    {
      id: 1,
      title: "Project Alpha",
      description: "A placeholder project demonstrating a web application built with Next.js and FastAPI.",
      link: "#",
    },
    {
      id: 2,
      title: "Project Beta",
      description: "Another placeholder project showcasing a data visualization tool using Python and a React frontend.",
      link: "#",
    },
    {
      id: 3,
      title: "Project Gamma",
      description: "A third placeholder project, this one focusing on a mobile-first design with a serverless backend.",
      link: "#",
    },
  ];

  return (
    <section className="py-8">
      <h2 className="text-3xl font-bold mb-4">Developer Portfolio</h2>
      <div className="space-y-8">
        {projects.map((project) => (
          <article key={project.id} className="border-b pb-4">
            <h3 className="text-2xl font-bold mb-2">{project.title}</h3>
            <p className="text-lg mb-2">{project.description}</p>
            <a href={project.link} target="_blank" rel="noopener noreferrer" className="text-blue-500 hover:underline">View Project</a>
          </article>
        ))}
      </div>
    </section>
  );
}
