# Hi, I'm dunamismax

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Go_Logo_Blue.svg/1920px-Go_Logo_Blue.svg.png" alt="The Go programming language logo." width="150"/>
</p>

<p align="center">
  <a href="https://github.com/dunamismax">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=24&pause=1000&color=00ADD8&center=true&vCenter=true&width=800&lines=IT+Director+%7C+Go+Developer;Creator+of+The+Go-Pragmatic+Stack;Go+%2B+Gin+%2B+sqlc+%2B+htmx;A+Robust+Toolkit+for+Modern+Apps;Explore+my+reference+implementation+below!" alt="Typing SVG" />
  </a>
</p>

Hello! Thanks for stopping by.

I'm an IT Director with over a decade of experience, but my true passion is the craft of software development—especially with Go. I'm driven by its power to create incredibly fast, single-binary applications that are a joy to deploy and maintain.

This journey led me to create **The Go-Pragmatic Stack**, my official architecture for building best-in-class, modern web applications. It's a complete, opinionated blueprint for creating highly performant and maintainable software. It pairs a powerful Go backend with a modern, server-centric frontend toolchain, providing a structured and scalable environment without unnecessary complexity.

I share my work and reference implementations freely, hoping to help others build better, faster software. If my projects have helped you out, I'd be incredibly grateful if you'd consider supporting my work with a coffee.

It makes a huge difference!

---

### My Go Toolkit

My toolkit is a reflection of the Go-Pragmatic stack: focused on performance, simplicity, and a superior developer experience with Go at the core.

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=go,nodejs,tailwind,htmx,sqlite,linux,ubuntu" />
  </a>
</p>

<details>
<summary><h3>The Go-Pragmatic Stack (Click to Expand)</h3></summary>

This stack represents a complete, best-in-class architecture for building secure, observable, and maintainable web applications. It is composed of a powerful Go backend and a modern, server-centric frontend toolchain. The stack prioritizes simplicity, rapid development, and zero-dependency deployment by favoring Go's native capabilities and lightweight, embedded tools.

---

### **Frontend**

The frontend architecture uses a modern build system and a server-centric interactivity model to deliver a fast, responsive, and maintainable user experience with minimal client-side complexity.

- [**esbuild**](https://esbuild.github.io/getting-started/)
  - **Role:** Asset Bundler & Minifier.
  - **Description:** An extremely fast JavaScript and CSS bundler written in Go. It processes frontend assets, handles module bundling, and performs minification, ensuring a highly optimized production output while maintaining a rapid development feedback loop.
- [**PostCSS**](https://postcss.org/docs/postcss-cli)
  - **Role:** CSS Processor.
  - **Description:** A tool for transforming CSS with JavaScript plugins. It is essential for processing the Tailwind CSS framework, running as part of the build step to compile utility classes and custom directives into a standard, browser-ready stylesheet.
- [**Tailwind CSS**](https://tailwindcss.com/docs/installation)
  - **Role:** Utility-First CSS Framework.
  - **Description:** A highly-customizable, utility-first CSS framework that enables rapid UI development directly within the HTML markup. It promotes design consistency and produces a minimal CSS file for production.
- [**HTMX**](https://htmx.org/docs/)
  - **Role:** Server-Centric Interactivity.
  - **Description:** A powerful library that enables modern browser features like AJAX and dynamic content updates directly from HTML attributes. It allows the backend to deliver UI fragments over the wire, providing rich user experiences without complex client-side JavaScript.
- [**Go `html/template`**](https://pkg.go.dev/html/template)
  - **Role:** Secure HTML Templating.
  - **Description:** The official Go standard library for creating HTML templates. It provides secure, context-aware automatic escaping to prevent Cross-Site Scripting (XSS) attacks, making it a robust and idiomatic choice for server-side rendering of HTML pages and HTMX partials.
- [**Alpine.js**](https://alpinejs.dev/start-here)
  - **Role:** Lightweight Client-Side Interactivity.
  - **Description:** A rugged, minimal framework for composing JavaScript behavior directly in your HTML markup. It serves as the perfect lightweight companion to HTMX for handling small client-side interactions like dropdowns, modals, and toggles, without requiring a heavy client-side framework.

---

### **Backend**

A lean, performant, and maintainable backend service architected for rapid development and long-term stability.

- [**Go**](https://go.dev/doc/)
  - **Role:** Backend Language.
  - **Description:** A statically typed, compiled language renowned for its performance, concurrency, and simplicity. Its ability to compile to a single binary simplifies deployment.
- [**Gin**](https://gin-gonic.com/docs/)
  - **Role:** High-Performance Web Framework.
  - **Description:** A popular and fast HTTP web framework for Go, offering a rich feature set including routing, middleware, and JSON validation, which helps accelerate API development.
- [**`go-playground/validator`**](https://pkg.go.dev/github.com/go-playground/validator/v10)
  - **Role:** Struct Validation.
  - **Description:** The de-facto standard for data validation using struct tags. It ensures data integrity by validating incoming request data at the application's edge.
- [**`koanf`**](https://github.com/knadh/koanf)
  - **Role:** Lightweight & Flexible Configuration.
  - **Description:** A minimal and modular configuration management library. It provides a clean API for reading configuration from various sources like files and environment variables with a small dependency footprint, making it a simple and maintainable choice.
- [**`log/slog`**](https://pkg.go.dev/log/slog)
  - **Role:** Structured Logging.
  - **Description:** The official structured logging library in the Go standard library. It produces consistent, machine-readable logs essential for effective monitoring and debugging.

---

### **Database & Caching**

A zero-dependency, in-process data layer that maximizes simplicity and speed for a wide range of applications.

- [**SQLite**](https://www.sqlite.org/docs.html)
  - **Role:** Embedded Relational Database.
  - **Description:** A self-contained, serverless, full-featured SQL database engine that runs in-process with the application. It reads and writes to a single file, eliminating operational overhead and making it perfect for local development, testing, and many production workloads.
- [**`sqlc`**](https://docs.sqlc.dev/)
  - **Role:** Type-Safe SQL to Go Code Generation.
  - **Description:** A tool that generates fully type-safe, idiomatic Go code from raw SQL queries. This allows developers to write performant, handcrafted SQL while eliminating manual boilerplate and preventing data-related bugs at compile time.
- [**`golang-migrate/migrate`**](https://github.com/golang-migrate/migrate/blob/master/MIGRATIONS.md)
  - **Role:** Database Schema Migrations.
  - **Description:** A robust and widely-used tool for managing and applying versioned SQL schema migrations. Migrations can be written in plain SQL and sourced from files, ensuring database schemas evolve predictably.
- [**`go-cache`**](https://pkg.go.dev/github.com/patrickmn/go-cache)
  - **Role:** In-Process Caching.
  - **Description:** A simple, thread-safe in-memory key-value store with expiration times. It provides extremely fast caching capabilities without requiring any external dependencies or network overhead.

---

### **CLI, Development & Deployment**

A professional and minimalist toolchain for a smooth developer workflow and consistent builds.

- [**`ffcli`**](https://pkg.go.dev/github.com/peterbourgon/ff/v3/ffcli) & [**`promptui`**](https://github.com/manifoldco/promptui)
  - **Role:** Lightweight CLI & TUI Frameworks.
  - **Description:** `ffcli` provides a minimal, composable framework for building traditional CLI applications, while `promptui` enables the creation of simple, interactive terminal prompts for user input.
- [**`stretchr/testify`**](https://pkg.go.dev/github.com/stretchr/testify)
  - **Role:** Testing Toolkit.
  - **Description:** A suite of packages providing a fluent, expressive API for writing tests, including assertions, mocking, and test suite management.
- [**Mage**](https://magefile.org/)
  - **Role:** Go-Native Task Runner / Build System.
  - **Description:** A build tool that allows you to write build scripts and tasks in plain Go, providing a type-safe, cross-platform, and idiomatic way to orchestrate all development workflows without leaving the Go ecosystem.
- [**Air**](https://github.com/cosmtrek/air)
  - **Role:** Live Reloading.
  - **Description:** A development utility that watches for file changes and automatically recompiles and restarts the server, providing a rapid feedback loop.
- [**Caddy**](https://caddyserver.com/docs/)
  - **Role:** Web Server & Reverse Proxy.
  - **Description:** A modern web server with automatic HTTPS. It serves static frontend assets and acts as a secure reverse proxy for the Go application.

---

### **CI/CD**

A fully automated pipeline for building, testing, and deploying the application, ensuring consistency and quality.

- [**GitHub Actions**](https://docs.github.com/en/actions)
  - **Role:** Automated CI/CD Platform.
  - **Description:** A CI/CD workflow defined in the project repository to automate the entire lifecycle. The pipeline performs:
    - **Linting & Formatting:** Runs `golangci-lint` and `gofmt` to enforce code quality.
    - **Testing:** Executes unit and integration tests using `go test`.
    - **Vulnerability Scanning:** Runs `govulncheck` to scan for security vulnerabilities.
    - **Build:** Compiles the application and builds frontend assets using a `Mage` task.

</details>

---

<p align="center">
  <img src="https://user-images.githubusercontent.com/3185864/32058716-5ee9b512-ba38-11e7-978a-287eb2a62743.png" alt="Gopher Mage." width="150"/>
</p>

### My Current Focus: The Go-Pragmatic Reference Implementation

My **Go-Pragmatic** monorepo serves as the official reference implementation for **The Go-Pragmatic Stack**. It is the central hub where I put my architectural philosophy into practice, creating a living testament to the power and elegance of this approach.

<p align="center">
  <a href="https://github.com/dunamismax/Go-Pragmatic">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=dunamismax&repo=Go-Pragmatic&theme=dracula&show_owner=true" alt="Reference Implementation for The Go-Pragmatic Stack" />
  </a>
</p>

---

### Support My Work

If you find my work on this stack valuable, consider supporting me. It helps me dedicate more time to creating and maintaining open-source projects.

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
