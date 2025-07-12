<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Go_Logo_Blue.svg/1920px-Go_Logo_Blue.svg.png" alt="The Go programming language logo." width="150"/>
</p>

<p align="center">
  <a href="https://github.com/dunamismax/go-modern-scaffold">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=24&pause=1000&color=00ADD8&center=true&vCenter=true&width=800&lines=IT+Director+%7C+Go+Developer;Creator+of+The+Go-Modern+Stack;Go+%2B+Fiber+%2B+HTMX+%2B+Tailwind;Interactive%2C+Performant%2C+and+Beautiful;Clone%2C+Configure%2C+and+Deploy!" alt="Typing SVG" />
  </a>
</p>

With over a decade of IT experience, I specialize in building fast, maintainable, and powerful applications with Go. I have authored two distinct, production-ready Go stacks to suit different development philosophies:

1. **[The Go-Modern Stack](https://github.com/dunamismax/go-modern-scaffold)**: A feature-rich, batteries-included architecture for building highly interactive and visually appealing web applications with maximum velocity.
2. **[The Pure Go Standard Library Stack](https://github.com/dunamismax/go-stdlib-scaffold)**: A minimalist, dependency-free blueprint for developers who value ultimate simplicity and long-term stability.

Both stacks are available as ready-to-clone templates, each with a complete and self-contained development ecosystem orchestrated by a powerful `magefile.go`.

---

### My Featured Scaffolds

These repositories are the official reference implementations for my two Go stacks. They are living projects that serve as powerful, real-world templates for building robust web applications.

<p align="center">
  <a href="https://github.com/dunamismax/go-modern-scaffold">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=dunamismax&repo=go-modern-scaffold&theme=dracula&show_owner=true" alt="go-modern-scaffold Repository" />
  </a>
  <a href="https://github.com/dunamismax/go-stdlib-scaffold">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=dunamismax&repo=go-stdlib-scaffold&theme=dracula&show_owner=true" alt="go-stdlib-scaffold Repository" />
  </a>
</p>

---

<p align="center">
  <img src="https://user-images.githubusercontent.com/3185864/32058716-5ee9b512-ba38-11e7-978a-287eb2a62743.png" alt="Gopher Mage." width="150"/>
</p>

### The Ultimate Workflow: The `Magefile`

One of the standout features of both scaffold templates is the **`magefile.go`**. This isn't just a build script; it's a complete, Go-native task runner that orchestrates the entire development lifecycle. It provides a seamless, cross-platform experience without ever leaving the Go ecosystem.

**Why is it so great?**

- **Simplicity:** Manage complex workflows with simple commands like `mage dev` or `mage check:all`.
- **Consistency:** Ensures every developer on a project uses the exact same commands for building, testing, and quality checks.
- **Extensibility:** It's written in pure Go, making it easy to customize and extend for any project-specific needs.

With a single command, you can run a comprehensive suite of tests, build production-ready binaries, and manage database migrations. It's designed to make you productive from the very first minute.

---

### My Go Toolkit

My toolkit is a reflection of the two stacks I've created: one focused on a rich, modern toolset and the other on pure, dependency-free simplicity. Both are centered around a superior developer experience with Go at the core.

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=go,fiber,tailwind,docker,postgres,redis,sqlite,linux,ubuntu" />
  </a>
</p>

<details open>
<summary><h3>The Go-Modern Stack (Click to Expand)</h3></summary>

---

This stack is architected for developers aiming to build feature-rich, visually appealing, and highly interactive web and command-line applications with Go. It strategically combines powerful, community-vetted libraries with core Go idioms for a productive and ergonomic development experience. The result is a stack that prioritizes speed, type safety, and modern design without compromising on the core strengths of Go.

---

### **Frontend: Rich, Interactive & Beautifully Styled**

This frontend architecture is designed for building modern, animated user experiences with maximum velocity. It combines a Go-native templating engine with a complete ecosystem for styling, component-building, and interactivity, enabling the rapid development of dynamic and polished interfaces.

- [**Templ**](https://templ.guide/)
  - **Role:** Type-Safe, Component-Based HTML Templating.
  - **Description:** A modern templating language that generates Go code from your components, providing compile-time type safety for your HTML. It allows you to build encapsulated, reusable UI elements with pure Go logic, eliminating runtime errors common in string-based templates.
- [**Tailwind CSS**](https://tailwindcss.com/docs/installation)
  - **Role:** Utility-First CSS Framework.
  - **Description:** Enables incredibly fast UI development by providing low-level utility classes that can be composed to build any design directly within your HTML. This removes the need for writing custom CSS and ensures a consistent, scalable styling system.
- [**DaisyUI**](https://daisyui.com/)
  - **Role:** Component Library for Tailwind CSS.
  - **Description:** A plugin for Tailwind CSS that provides a rich set of pre-built, themeable components like buttons, cards, and modals. It drastically speeds up development by allowing you to use simple class names (e.g., `btn-primary`) instead of long strings of utilities.
- [**HTMX**](https://htmx.org/docs/)
  - **Role:** HTML-driven Interactivity.
  - **Description:** Adds dynamic, AJAX-powered interactivity to your application with simple HTML attributes. It allows server-side rendered applications to feel as responsive as a single-page app (SPA) without writing complex JavaScript.
- [**Hyperscript**](https://hyperscript.org/)
  - **Role:** Expressive, Event-Driven Scripting.
  - **Description:** A scripting language designed for modern web development that lives directly in your HTML. It uses an intuitive, English-like syntax to handle user events and DOM manipulations, making it a natural companion to HTMX for client-side interactivity.
- [**HTMX CSS Transitions**](https://htmx.org/examples/animation/)
  - **Role:** Native, Lightweight Animations.
  - **Description:** Leverage HTMX's built-in support for CSS transitions to create smooth animations between page states. By default, HTMX adds classes during its lifecycle, allowing you to easily apply fades, slides, and other effects with pure CSS.
- [**Animate.css**](https://animate.style/)
  - **Role:** Drop-in CSS Animation Library.
  - **Description:** A library of ready-to-use, cross-browser CSS animations. It provides an extensive collection of effects that can be easily triggered by Hyperscript or HTMX events to add polish and visual feedback to your interface.

---

### **Backend: Ergonomic, Performant & Well-Structured**

This backend is built for developer productivity and robust performance, leveraging a high-speed web framework and best-in-class libraries for logging, configuration, and validation.

- [**Fiber**](https://docs.gofiber.io/)
  - **Role:** High-Performance Web Framework.
  - **Description:** An Express.js-inspired web framework built on top of Fasthttp, Go's fastest HTTP engine. It is designed for high-performance and zero memory allocation, providing a developer-friendly API for building APIs and web services rapidly.
- [**slog**](https://pkg.go.dev/log/slog)
  - **Role:** Structured, Level-Based Logging.
  - **Description:** The official structured logging package in Go's standard library. It enables the creation of machine-readable, key-value pair logs with severity levels, which is essential for effective parsing, filtering, and analysis in modern observability platforms.
- [**Viper**](https://github.com/spf13/viper)
  - **Role:** Complete Configuration Management.
  - **Description:** A comprehensive configuration solution for Go applications. Viper can manage configuration from various sources—including YAML, JSON, and TOML files, environment variables, and remote key-value stores—unifying them into a single, accessible interface.
- [**Validator**](https://pkg.go.dev/github.com/go-playground/validator/v10)
  - **Role:** Struct-Tag Based Data Validation.
  - **Description:** The de-facto standard for data validation in Go. It enables declarative validation on struct fields using simple tags (e.g., `validate:"required,email"`), integrating seamlessly with frameworks like Fiber to ensure data integrity.

---

### **TUI (Terminal User Interface): Beautiful & Interactive Command-Line Apps**

For building polished and modern command-line applications, the [**Charm Bracelet**](https://charm.sh/) ecosystem provides a complete and elegant solution.

- [**Bubble Tea**](https://github.com/charmbracelet/bubbletea)
  - **Role:** Stateful TUI Framework.
  - **Description:** Brings The Elm Architecture (a functional, model-view-update pattern) to terminal applications, making it ideal for building complex, interactive, and stateful TUIs that are easy to reason about and maintain.
- [**Bubbles**](https://github.com/charmbracelet/bubbles)
  - **Role:** Reusable TUI Components.
  - **Description:** A library of common, ready-to-use TUI components—such as spinners, text inputs, and tables—that are designed to work with Bubble Tea, dramatically accelerating the development of sophisticated interfaces.
- [**Lipgloss**](https://github.com/charmbracelet/lipgloss)
  - **Role:** Declarative Terminal Styling.
  - **Description:** Offers a fluent, expressive API for styling terminal text. It makes it simple to define colors, layouts, borders, and margins, enabling you to design beautiful and readable TUIs with ease.

---

### **Database & Caching: Type-Safe, Performant & Scalable**

This data layer is optimized for performance and maintainability by pairing direct SQL control with generated, type-safe Go code and a modern, declarative schema migration tool.

- [**sqlc**](https://docs.sqlc.dev/)
  - **Role:** Type-Safe SQL Code Generation.
  - **Description:** Generates fully type-safe, idiomatic Go code from your SQL schema and queries. This allows you to write raw SQL for maximum control and performance while benefiting from compile-time safety, eliminating an entire class of runtime database errors.
- [**Atlas**](https://atlasgo.io/)
  - **Role:** Database Schema Migrations.
  - **Description:** A modern, language-agnostic tool for managing and migrating database schemas. Atlas can automatically generate migration plans by comparing the desired schema (defined in HCL, SQL, or ORM) to the database's current state, streamlining schema evolution with a declarative workflow.
- [**Ristretto**](https://github.com/dgraph-io/ristretto)
  - **Role:** High-Performance In-Process Cache.
  - **Description:** A fast, concurrent, and memory-bounded in-process cache from Dgraph. It is designed to achieve high hit ratios with low memory overhead, making it an excellent choice for performance-critical caching within a single application instance.
- [**go-redis**](https://redis.io/docs/clients/go/)
  - **Role:** Redis Client for Distributed Caching.
  - **Description:** The premier Go client for Redis, providing a high-performance interface for all Redis features. It is essential for implementing a distributed cache, which is critical for scaling applications that require shared state or session management.

---

### **Development Workflow: Automated, Rapid & High-Quality**

A modern toolchain using best-in-class tools to automate common tasks, ensure code quality, and maintain a fast and efficient developer feedback loop.

- [**Mage**](https://magefile.org/)
  - **Role:** Task Runner / Build System.
  - **Description:** An elegant, Make-like tool that allows you to define build tasks (like compiling, testing, or linting) as simple Go functions within a `magefile.go`. This provides a clean, cross-platform, and idiomatic way to automate your project's workflow.
- [**Air**](https://github.com/cosmtrek/air)
  - **Role:** Live Reloading for Development.
  - **Description:** A powerful command-line utility that watches for file changes in your project and automatically recompiles and restarts your application. Air provides a rapid, real-time feedback loop that is essential for productive web development.
- [**GolangCI-Lint**](https://golangci-lint.run/)
  - **Role:** Code Quality Linter Aggregator.
  - **Description:** A fast, configurable linter that runs many Go linters in parallel. It analyzes source code for stylistic issues, bugs, and complexities, enforcing code quality and consistency across the entire project.
- [**Prettier Tailwind CSS Plugin**](https://github.com/tailwindlabs/prettier-plugin-tailwindcss)
  - **Role:** Automatic Class Sorting.
  - **Description:** An official Prettier plugin that automatically sorts your Tailwind CSS classes in a consistent, logical order. This keeps your HTML clean and readable, significantly improving maintainability with zero manual effort.

---

### **Testing: Idiomatic & Dependency-Free**

This stack relies exclusively on Go's powerful, built-in testing framework to ensure code quality and correctness without external dependencies.

- [**Go `testing` Package**](https://pkg.go.dev/testing)
  - **Role:** Core Testing Framework.
  - **Description:** Go's standard library for writing unit, integration, and benchmark tests. Assertions are handled with simple `if` statements and `t.Errorf`, which keeps tests explicit, clear, and easy to maintain while avoiding third-party dependencies.

</details>

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

If you find my work on these Go stacks valuable, please consider supporting me. It helps me dedicate more time to creating and maintaining high-quality open-source projects.

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
