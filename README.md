# Hi, I'm dunamismax

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Go_Logo_Blue.svg/1920px-Go_Logo_Blue.svg.png" alt="The Go programming language logo." width="150"/>
</p>

<p align="center">
  <a href="https://github.com/dunamismax/go-stdlib-scaffold">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=24&pause=1000&color=00ADD8&center=true&vCenter=true&width=800&lines=IT+Director+%7C+Go+Developer;Creator+of+go-stdlib-scaffold;A+Dependency-Free+Go+Blueprint;Go+%2B+net/http+%2B+database/sql;Clone%2C+Configure%2C+and+Deploy!" alt="Typing SVG" />
  </a>
</p>

With over a decade of IT experience, I specialize in building fast, maintainable, and dependency-free applications with Go. To promote long-term stability and ultimate simplicity, I created **[go-stdlib-scaffold](https://github.com/dunamismax/go-stdlib-scaffold)**—an opinionated, production-ready blueprint that runs on nothing but Go's standard library.

This repository is the culmination of my philosophy: a ready-to-clone template that demonstrates the power and elegance of a pure Go backend. It's built on **The Pure Go Standard Library Stack** and is designed for developers who value performance, minimalism, and a zero-dependency workflow.

---

### My Featured Project: `go-stdlib-scaffold`

My **[go-stdlib-scaffold](https://github.com/dunamismax/go-stdlib-scaffold)** repository is a living project that serves as a powerful, real-world template for building robust web applications using only the tools provided by Go itself. It's more than just a collection of files; it's a complete and self-contained development ecosystem.

<p align="center">
  <a href="https://github.com/dunamismax/go-stdlib-scaffold">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=dunamismax&repo=go-stdlib-scaffold&theme=dracula&show_owner=true" alt="go-stdlib-scaffold Repository" />
  </a>
</p>

---

<p align="center">
  <img src="https://user-images.githubusercontent.com/3185864/32058716-5ee9b512-ba38-11e7-978a-287eb2a62743.png" alt="Gopher Mage." width="150"/>
</p>

### The Ultimate Workflow: The `Magefile`

One of the standout features of the `go-stdlib-scaffold` template is its **`magefile.go`**. This isn't just a build script; it's a complete, Go-native task runner that orchestrates the entire development lifecycle. It provides a seamless, cross-platform experience without ever leaving the Go ecosystem.

**Why is it so great?**

- **Simplicity:** Manage complex workflows with simple commands like `mage run` or `mage check:all`.
- **Consistency:** Ensures every developer on a project uses the exact same commands for building, testing, and quality checks.
- **Extensibility:** It's written in pure Go, making it easy to customize and extend for any project-specific needs.

With a single command, you can run a comprehensive suite of tests, build production-ready binaries, and manage database migrations. It's designed to make you productive from the very first minute.

---

### My Go Toolkit

My toolkit is a reflection of The Pure Go Standard Library Stack, which powers `go-stdlib-scaffold`: focused on performance, simplicity, and a superior developer experience with Go at the core.

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=go,sqlite,linux,ubuntu" />
  </a>
</p>

<details>
<summary><h3>The Pure Go Standard Library Stack (Click to Expand)</h3></summary>

---

This stack represents a minimalist, robust architecture for building secure and performant web applications. It is composed entirely of a Go backend that leverages the standard library, removing all external dependencies. The stack prioritizes ultimate simplicity, zero-dependency deployment, and long-term stability by relying exclusively on Go's continuously evolving native capabilities. The frontend is reduced to plain HTML and CSS, with no JavaScript.

---

### **Frontend**

The frontend architecture is intentionally simplified to its core components, delivering a fast, accessible, and extremely maintainable user experience by avoiding all client-side scripting and build tools.

- [**Go `html/template`**](https://pkg.go.dev/html/template)
  - **Role:** Secure HTML Templating.
  - **Description:** Go's standard library for server-side HTML rendering. It provides automatic, context-aware escaping to prevent Cross-Site Scripting (XSS). As of Go 1.24, it also supports `range-over-func` and `range-over-int`, allowing for more flexible iteration patterns directly within templates.
- [**Plain CSS**](https://developer.mozilla.org/en-US/docs/Web/CSS)
  - **Role:** Styling.
  - **Description:** A standard, handwritten CSS file served as a static asset. This approach removes the need for pre-processors or build steps, maximizing simplicity and performance.

---

### **Backend**

A lean, highly performant, and secure backend service architected using only the Go standard library for maximum stability and minimal attack surface.

- [**Go (1.24+)**](https://go.dev/doc/)
  - **Role:** Backend Language.
  - **Description:** A statically typed, compiled language known for performance, concurrency, and simplicity. The Go 1.22+ `for` loop semantics prevent common concurrency bugs by creating new variables for each iteration. It compiles to a single, dependency-free binary, streamlining deployment.
- [**`net/http`**](https://pkg.go.dev/net/http)
  - **Role:** Web Server & Advanced Routing.
  - **Description:** The standard library's package for all HTTP-related tasks. As of Go 1.22, the `http.ServeMux` includes an enhanced request router that supports method-based routing (e.g., `POST /items`) and wildcards (e.g., `/items/{id}`), removing the need for third-party frameworks. Path values are easily accessed via `r.PathValue("id")`.
- [**Custom Validation Functions**](https://www.alexedwards.net/blog/validation-snippets-for-go)
  - **Role:** Data Validation.
  - **Description:** Data validation is handled by simple, explicit Go functions. Go 1.24's full support for generic type aliases allows for more reusable and readable validation logic.
- [**`os`**](https://pkg.go.dev/os)
  - **Role:** Secure Filesystem Access & Environment Loading.
  - **Description:** Configuration is loaded from environment variables using `os.Getenv`. For file operations, Go 1.24's `os.Root` provides directory-limited filesystem access, preventing directory traversal attacks and ensuring that file-serving or upload handlers operate within a secure boundary.

---

### **Database & Caching**

A zero-dependency, in-process data layer that maximizes simplicity and speed by using Go's native database interface and advanced concurrency and memory primitives.

- [**SQLite**](https://www.sqlite.org/docs.html)
  - **Role:** Embedded Relational Database.
  - **Description:** A self-contained, serverless SQL database engine that runs in-process, eliminating operational overhead and making it ideal for a wide range of production workloads.
- [**`database/sql`**](https://pkg.go.dev/database/sql)
  - **Role:** SQL Database Interface.
  - **Description:** The standard library’s lean interface for SQL databases. As of Go 1.22, it includes the generic `sql.Null[T]` type, which simplifies scanning nullable columns, reduces boilerplate, and improves type safety.
- [**SQL/Go Migration Scripts**](https://amacneil.github.io/dbmate/2022/01/21/go-database-migrations-without-orm.html)
  - **Role:** Database Schema Migrations.
  - **Description:** Migrations are managed with numbered SQL files or simple Go programs using `database/sql`. The concise `for i := range 10` syntax from Go 1.22 can simplify scripting.
- [**`sync`, `maps` & `unique`**](https://pkg.go.dev/sync)
  - **Role:** High-Performance In-Process Caching.
  - **Description:** High-performance, in-process caching is achieved with a standard Go map and a `sync.RWMutex`. As of Go 1.24, map performance is significantly improved due to a new Swiss Table implementation, directly boosting cache speed. For further memory optimization, Go 1.23's `unique` package can be used to canonicalize cache keys or values, reducing memory footprint.

---

### **Testing**

A robust testing suite that relies exclusively on Go's powerful, built-in testing framework to ensure code quality and correctness.

- [**`testing`**](https://pkg.go.dev/testing)
  - **Role:** Core Testing Framework.
  - **Description:** The built-in package for unit, integration, and benchmark tests. Go 1.24's `go vet` includes a new `tests` analyzer that identifies common mistakes in test declarations. Assertions use simple `if` statements with `t.Errorf`, keeping tests clear and dependency-free.

---

### **CLI, Development & Deployment**

A minimalist and modern toolchain using built-in Go commands and standard, universally available tools for a smooth developer workflow.

- [**`flag`**](https://pkg.go.dev/flag)
  - **Role:** Command-Line Interface.
  - **Description:** The standard library's package for parsing command-line options. It is sufficient for building CLIs for most applications without third-party dependencies.
- [**Mage / Magefile (with `go.mod` toolchain)**](https://magefile.org/)
  - **Role:** Task Runner / Build System.
  - **Description:** As of Go 1.24, Mage and other build tools are managed declaratively via `tool` directives in the `go.mod` file. This replaces the `tools.go` workaround and ensures version-locked, reproducible builds across all development and CI environments.
- [**Simple Shell Scripts**](https://dev.to/ignatk/go-live-reloading-with-a-shell-script-2305)
  - **Role:** Live Reloading.
  - **Description:** During development, a simple shell script can watch for file changes, automatically recompiling and restarting the server for a rapid feedback loop.

---

### **CI/CD**

A fully automated, robust pipeline using modern Go tooling to build, test, and deploy the application, ensuring consistency and quality.

- [**GitHub Actions**](https://docs.github.com/en/actions)
  - **Role:** Automated CI/CD Platform.
  - **Description:** A CI/CD workflow defined in the project repository automates the entire lifecycle. The pipeline performs:
    - **Linting & Formatting:** Runs `gofmt` and `go vet` to enforce code style and identify issues.
    - **Testing:** Executes the test suite with `go test -json`, which (as of Go 1.24) provides structured JSON output for reliable, machine-readable test results.
    - **Vulnerability Scanning:** Runs `govulncheck` to scan for security vulnerabilities.
    - **Build:** Compiles the application into a single binary using `go build -json`, capturing structured build information for easier artifact management and error analysis.
- [**`go build` Scripts (via Magefile)**](https://www.digitalocean.com/community/tutorials/how-to-build-go-executables-for-multiple-platforms-on-ubuntu-20-04)
  - **Role:** Release Automation.
  - **Description:** A simple script using `go build` with different `GOOS` and `GOARCH` environment variables automates cross-compilation. Go 1.24 automatically embeds version control information into the binary for improved traceability. The build process benefits from Profile-Guided Optimization (PGO), whose build-time overhead was significantly reduced in Go 1.23.

</details>

---

### Support My Work

If you find my work on `go-stdlib-scaffold` and The Pure Go Standard Library Stack valuable, please consider supporting me. It helps me dedicate more time to creating and maintaining high-quality open-source projects.

<p align="center">
  <a href="https://coff.ee/dunamismax" target="_blank">
    <img src="https://raw.githubusercontent.com/egonelbre/gophers/master/.thumb/animation/buy-morning-coffee-3x.gif" alt="Buy Me a Coffee" />
  </a>
</p>

---

### Let's Connect

<p align="center">
  <a href="https://twitter.com/dunamismax" target="_blank"><img src="https://img.shields.io/badge/Twitter-%231DA1F2.svg?&style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter"></a>
  <a href="https://bsky.app/profile/dunamismax.bsky.social" target="_blank"><img src="https://img.shields.io/badge/Bluesky-blue?style=for-the-badge&logo=bluesky&logoColor=white" alt="Bluesky"></a>
  <a href="https://reddit.com/user/dunamismax" target="_blank"><img src="https://img.shields.io/badge/Reddit-%23FF4500.svg?&style=for-the-badge&logo=reddit&logoColor=white" alt="Reddit"></a>
  <a href="https://discord.com/users/dunamismax" target="_blank"><img src="https://img.shields.io/badge/Discord-dunamismax-7289DA.svg?style=for-the-badge&logo=discord&logoColor=white" alt="Discord"></a>
  <a href="https://signal.me/#p/+dunamismax.66" target="_blank"><img src="https://img.shields.io/badge/Signal-dunamismax.66-3A76F0.svg?style=for-the-badge&logo=signal&logoColor=white" alt="Signal"></a>
</p>

<p align="center">
    <img src="https://raw.githubusercontent.com/egonelbre/gophers/refs/heads/master/.thumb/animation/2bit-sprite/demo.gif" alt="Gopher Sprite Animation" />
</p>
