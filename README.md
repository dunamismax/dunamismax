# Hi, I'm dunamismax

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Go_Logo_Blue.svg/1920px-Go_Logo_Blue.svg.png" alt="The Go programming language logo." width="150"/>
</p>

<p align="center">
  <a href="https://github.com/dunamismax">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=24&pause=1000&color=00ADD8&center=true&vCenter=true&width=800&lines=IT+Director+%7C+Go+Developer;Creator+of+The+Go-Pragmatic+Stack;Go+%2B+Gin+%2B+sqlc+%2B+htmx;A+Robust+Toolkit+for+Modern+Apps;Explore+my+reference+implementation+below!" alt="Typing SVG" />
  </a>
</p>

With over a decade of IT experience, I specialize in building fast and maintainable single-binary applications with Go.

To streamline modern web development, I created The Go-Pragmatic Stack—an opinionated blueprint that pairs a high-performance Go backend with a responsive, server-centric frontend.

This philosophy is put into practice in my go-scaffold repository, which serves as a ready-to-use template for building robust applications based on this stack. If you find this project helpful, your support is greatly appreciated.

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
