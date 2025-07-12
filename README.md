# Hi, I'm dunamismax

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Go_Logo_Blue.svg/1920px-Go_Logo_Blue.svg.png" alt="The Go programming language logo." width="150"/>
</p>

<p align="center">
  <a href="https://github.com/dunamismax/go-scaffold">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=24&pause=1000&color=00ADD8&center=true&vCenter=true&width=800&lines=IT+Director+%7C+Go+Developer;Creator+of+go-scaffold;A+Production-Ready+Go+Blueprint;Go+%2B+Chi+%2B+GORM+%2B+htmx;Clone%2C+Configure%2C+and+Deploy!" alt="Typing SVG" />
  </a>
</p>

With over a decade of IT experience, I specialize in building fast, maintainable, single-binary applications with Go. To streamline modern web development, I created **[go-scaffold](https://github.com/dunamismax/go-scaffold)**—an opinionated, production-ready blueprint designed to get you up and running instantly.

This repository is the culmination of my philosophy: a ready-to-clone template that pairs a high-performance Go backend with a responsive, server-centric frontend. It's built on **The Go-Pragmatic Stack** and is designed for developers who value simplicity, performance, and an elegant workflow.

---

### My Featured Project: `go-scaffold`

My **[go-scaffold](https://github.com/dunamismax/go-scaffold)** repository is a living project that serves as a powerful, real-world template for building robust web applications. It's more than just a collection of tools; it's a complete development ecosystem.

<p align="center">
  <a href="https://github.com/dunamismax/go-scaffold">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=dunamismax&repo=go-scaffold&theme=dracula&show_owner=true" alt="go-scaffold Repository" />
  </a>
</p>

---

<p align="center">
  <img src="https://user-images.githubusercontent.com/3185864/32058716-5ee9b512-ba38-11e7-978a-287eb2a62743.png" alt="Gopher Mage." width="150"/>
</p>

### The Ultimate Workflow: The `Magefile`

One of the standout features of the `go-scaffold` template is its **`magefile.go`**. This isn't just a build script; it's a complete, Go-native task runner that orchestrates the entire development lifecycle. It provides a seamless, cross-platform experience without ever leaving the Go ecosystem.

**Why is it so great?**

- **Simplicity:** Manage complex workflows with simple commands like `mage dev` or `mage check`.
- **Consistency:** Ensures every developer on a project uses the exact same commands for building, testing, and linting.
- **Extensibility:** It's written in pure Go, making it easy to customize and extend for any project-specific needs.

With a single command, you can spin up a live-reloading development environment, run a comprehensive suite of tests and linters, build production-ready binaries, and manage database migrations. It's designed to make you productive from the very first minute.

---

### My Go Toolkit

My toolkit is a reflection of the Go-Pragmatic stack, which powers `go-scaffold`: focused on performance, simplicity, and a superior developer experience with Go at the core.

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=go,nodejs,tailwind,htmx,sqlite,linux,ubuntu" />
  </a>
</p>

<details>
<summary><h3>The go-scaffold Stack (Click to Expand)</h3></summary>

This stack represents a complete, best-in-class architecture for building secure, observable, and maintainable web applications. It is composed of a powerful Go backend and a modern, server-centric frontend toolchain. The stack prioritizes simplicity, rapid development, and zero-dependency deployment by favoring Go's native capabilities and lightweight, embedded tools.

---

### **Frontend**

The frontend architecture uses a modern build system and a server-centric interactivity model to deliver a fast, responsive, and maintainable user experience with minimal client-side complexity.

- [**esbuild**](https://esbuild.github.io/getting-started/)
  - **Role:** Asset Bundler & Minifier.
  - **Description:** An extremely fast JavaScript and CSS bundler written in Go. It processes frontend assets, handles module bundling, and performs minification, ensuring a highly optimized production output while maintaining a rapid development feedback loop.
- [**PostCSS**](https://postcss.org/docs/)
  - **Role:** CSS Processor.
  - **Description:** A tool for transforming CSS with JavaScript plugins. It is essential for a build step that compiles utility classes and custom directives into a standard, browser-ready stylesheet.
- [**Tailwind CSS**](https://tailwindcss.com/docs/installation/using-vite)
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
- [**Chi**](https://go-chi.io/)
  - **Role:** Idiomatic & Lightweight Web Framework.
  - **Description:** A lightweight, idiomatic, and composable router for building Go HTTP services. It is built on the standard `net/http` library and is praised for its elegant design, providing powerful features like middleware, routing context, and graceful shutdowns without unnecessary overhead.
- [**`go-playground/validator`**](https://pkg.go.dev/github.com/go-playground/validator/v10)
  - **Role:** Struct Validation.
  - **Description:** The de-facto standard for data validation using struct tags. It ensures data integrity by validating incoming request data at the application's edge.
- [**godotenv**](https://pkg.go.dev/github.com/lpernett/godotenv)
  - **Role:** Environment Variable Loading.
  - **Description:** A library to load environment variables from a `.env` file. This is ideal for development, adhering to twelve-factor app principles by separating configuration from code without complicating local setup.

---

### **Database & Caching**

A zero-dependency, in-process data layer that maximizes simplicity and speed for a wide range of applications.

- [**SQLite**](https://www.sqlite.org/docs.html)
  - **Role:** Embedded Relational Database.
  - **Description:** A self-contained, serverless, full-featured SQL database engine that runs in-process with the application. It reads and writes to a single file, eliminating operational overhead and making it perfect for local development, testing, and many production workloads.
- [**GORM**](https://gorm.io/index.html)
  - **Role:** Developer-Friendly ORM.
  - **Description:** A comprehensive ORM library for Go that simplifies database interactions by mapping Go structs to database tables. It features auto-migrations, hooks, and transaction support, aiming to be developer-friendly.
- [**Goose**](https://pkg.go.dev/github.com/pressly/goose/v3)
  - **Role:** Database Schema Migrations.
  - **Description:** A robust tool for managing database schema evolution. It allows you to write migrations in either SQL or Go, providing flexibility for simple schema changes or complex data transformations.
- [**Ristretto**](https://pkg.go.dev/github.com/dgraph-io/ristretto)
  - **Role:** High-Performance In-Process Caching.
  - **Description:** A fast, concurrent, and memory-bounded in-process cache designed for high performance. It uses a sophisticated LFU-based admission policy to maximize hit ratios, providing a more robust and predictable caching solution for demanding workloads without external dependencies.

---

### **Testing**

A robust testing suite to ensure code quality, correctness, and maintainability.

- [**`go test`**](https://pkg.go.dev/testing)
  - **Role:** Core Testing Framework.
  - **Description:** The built-in Go testing command and package. It provides the foundation for writing unit, integration, and benchmark tests in a way that is simple and deeply integrated with the language.
- [**Testify**](https://github.com/stretchr/testify)
  - **Role:** Assertion & Mocking Toolkit.
  - **Description:** A toolkit that provides a rich set of assertion functions (`assert`, `require`) and an easy-to-use mocking framework. It significantly improves the readability and conciseness of tests, making them easier to write and maintain.

---

### **CLI, Development & Deployment**

A professional and minimalist toolchain for a smooth developer workflow and consistent builds.

- [**Urfave/CLI**](https://cli.urfave.org/)
  - **Role:** Feature-Rich CLI Framework.
  - **Description:** A declarative, fast, and dependency-free library for building command-line applications. It provides a simple API for creating apps with commands, subcommands, flags, and shell autocompletion, making it a powerful and accessible choice for any project.
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
    - **Testing:** Executes the test suite using `go test`, enhanced with `Testify` for expressive and readable assertions.
    - **Vulnerability Scanning:** Runs `govulncheck` to scan for security vulnerabilities.
    - **Build:** Compiles the application and builds frontend assets using a `Mage` task.
- [**GoReleaser**](https://goreleaser.com/customization/)
  - **Role:** Release Automation.
  - **Description:** A powerful tool that automates the entire release process. It seamlessly integrates with GitHub Actions to cross-compile Go binaries, create archives, generate changelogs, and publish releases, simplifying the delivery of software.

</details>

---

### Support My Work

If you find my work on `go-scaffold` and The Go-Pragmatic Stack valuable, please consider supporting me. It helps me dedicate more time to creating and maintaining high-quality open-source projects.

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
