<p align="center">
  <img src="https://github.com/dunamismax/full-stack-rust/blob/main/assets/rust-wallpaper-crab-new.png" alt="dunamismax - Full Stack Rust Developer" width="800"/>
</p>

<p align="center">
  <a href="https://github.com/dunamismax/full-stack-rust">
    <img src="https://readme-typing-svg.demolab.com/?font=Fira+Code&size=24&pause=1000&color=CE422B&center=true&vCenter=true&width=800&lines=IT+Director+%7C+Rust+Developer;Creator+of+Full+Stack+Rust;Actix+Web+%2B+Yew+%2B+SeaORM;Zero+JavaScript%2C+Maximum+Performance;Clone%2C+Configure%2C+and+Deploy!" alt="Typing SVG" />
  </a>
</p>

---

## <img src="https://github.com/dunamismax/full-stack-rust/blob/main/assets/rust-logo-solo.png" width="30" height="30"> About Me

With over a decade of IT experience, I specialize in building blazing-fast, memory-safe, and maintainable applications with Rust. I have created the **Full Stack Rust** monorepo - a production-grade reference implementation designed for maximum performance, type safety, and unified development across the entire technology stack.

**Focus**: Building complete applications using Rust everywhere - from WebAssembly frontends to high-performance backends, desktop apps, and CLI tools.

**Philosophy**:

- Single language across the entire stack
- Shared type-safe contracts between frontend and backend
- Zero-cost abstractions with memory safety
- Maximum code reuse through Cargo workspaces

---

## <img src="https://github.com/dunamismax/full-stack-rust/blob/main/assets/rust-crab-solo.png" width="30" height="30"> Featured Project

**[Full Stack Rust](https://github.com/dunamismax/full-stack-rust)** represents the zenith of unified development: a complete, self-contained stack that leverages Rust everywhere from WebAssembly frontends to high-performance backends, desktop applications, and command-line tools.

<p align="center">
  <a href="https://github.com/dunamismax/full-stack-rust">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=dunamismax&repo=full-stack-rust&theme=dracula&show_owner=true" alt="full-stack-rust Repository" />
  </a>
</p>

This repository serves as both a comprehensive reference implementation and a ready-to-clone template, featuring modern Rust development patterns with Cargo workspaces, shared libraries, and automated CI/CD workflows.

---

## <img src="https://github.com/dunamismax/full-stack-rust/blob/main/assets/rust-crab-solo.png" width="30" height="30"> The Cargo Workspace Advantage

The **Cargo workspace architecture** isn't just a monorepo; it's a complete, unified development environment that manages shared dependencies, enforces consistency, and enables maximum code reuse across applications.

**Why it's powerful**:

- **Unified Dependencies** - Centralized version management ensures consistency
- **Code Reuse** - Shared crates eliminate duplication between frontend, backend, desktop, and CLI
- **Type Safety** - Shared API contracts prevent frontend/backend type mismatches at compile time
- **Performance** - Zero-cost abstractions and memory safety without garbage collection overhead

With simple commands like `cargo run -p server` or `cargo tauri dev -p desktop`, you can instantly start any application in the stack.

---

## Tech Stack

My toolkit reflects the Full Stack Rust philosophy: a unified language approach that maximizes performance and safety while maintaining developer productivity.

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=rust,wasm,actix,sqlite,tauri,html,css,linux,ubuntu" />
  </a>
</p>

<details>
<summary><h3>Complete Technology Stack - Click to Expand</h3></summary>

This framework is designed for building high-performance, reliable, and maintainable applications using Rust across the entire stack. It prioritizes developer ergonomics, type safety, and a unified ecosystem, enabling you to go from frontend to deployment with a single language. It is engineered for building everything from dynamic web applications and APIs to powerful command-line and terminal tools.

---

### **Frontend: A Reactive, WebAssembly-Powered UI**

This frontend architecture leverages WebAssembly (WASM) to run native Rust code directly in the browser, delivering rich, interactive user experiences with near-native performance.

- [**Yew**](https://yew.rs/docs/getting-started):
  - **Role:** Component-Based Frontend Framework.
  - **Description:** Yew is a modern Rust framework for creating multi-threaded front-end web apps using WebAssembly. It features a component-based model and an `html!` macro similar to JSX, making it familiar for developers with a background in frameworks like React.
- [**Tauri**](https://tauri.app/v1/guides/):
  - **Role:** Cross-Platform Application Toolkit.
  - **Description:** Tauri packages your Yew web frontend into a lightweight, secure, and fast desktop application. It provides the native shell for your UI, enabling access to system resources, creating installers, and managing application updates for Windows, macOS, and Linux.
- [**Stylist**](https://docs.rs/stylist/latest/stylist/):
  - **Role:** CSS-in-Rust Styling.
  - **Description:** Stylist provides a type-safe, component-scoped styling solution for Rust-based WebAssembly applications. It integrates directly with Yew via a feature flag and allows you to write CSS within your components for co-located and maintainable styles.

---

### **Backend: High-Performance & Asynchronous**

This backend foundation is optimized for speed, memory safety, and high concurrency, built on Rust's powerful asynchronous ecosystem.

- [**Actix Web**](https://actix.rs/docs/):
  - **Role:** Powerful & Pragmatic Web Framework.
  - **Description:** A high-performance framework for building APIs and web services. Built on the actor model, Actix Web is capable of handling a massive number of concurrent connections with minimal resource usage, making it perfect for demanding backend services.
- [**Tokio**](https://tokio.rs/tokio/tutorial):
  - **Role:** Asynchronous Runtime.
  - **Description:** Tokio is the de-facto standard for writing asynchronous applications in Rust. It provides the non-blocking I/O platform, task scheduler, and utilities that power the entire backend, from Actix Web to database clients.
- [**Serde**](https://serde.rs/):
  - **Role:** Robust Data Serialization & Deserialization.
  - **Description:** A powerful and generic framework for converting Rust data structures to and from formats like JSON, BSON, and more. Serde is the essential tool for handling data in any modern web application.

---

### **Database & Data Handling**

This data layer is designed for reliability and seamless integration with the Rust ecosystem, offering choices for both development and production.

- [**SeaORM**](https://www.sea-ql.org/SeaORM/docs/internal-architecture/architecture):
  - **Role:** Relational ORM.
  - **Description:** A dynamic and flexible Object-Relational Mapper that helps you work with databases in an idiomatic Rust fashion. It reduces boilerplate and prevents common errors by mapping database tables to Rust structs.
- [**SQLite (via `sea-orm`'s driver)**](https://www.sqlite.org/docs.html):
  - **Role:** Embedded Database.
  - **Description:** A self-contained, file-based SQL database that requires no setup. It is the ideal choice for rapid development, testing, and applications that require an embedded database.

---

### **Authentication & Security**

A direct and explicit approach to security, providing robust tools to control the authentication and authorization flow in your application.

- [**actix-web-grants**](https://docs.rs/actix-web-grants/latest/actix_web_grants/):
  - **Role:** Flexible Authorization for Actix Web.
  - **Description:** Provides a flexible authorization layer to protect endpoints based on user roles and permissions. It can be integrated with various authentication schemes.
- [**jsonwebtoken**](https://docs.rs/jsonwebtoken/latest/jsonwebtoken/):
  - **Role:** Stateless JWT Authentication.
  - **Description:** A crate for creating and verifying JSON Web Tokens (JWTs), the standard for implementing stateless authentication in modern APIs. This is a powerful alternative to traditional session management.
- [**actix-identity**](https://docs.rs/actix-identity/latest/actix_identity/) & [**actix-session**](https://docs.rs/actix-session/latest/actix_session/):
  - **Role:** Session Management and User Identity.
  - **Description:** These middlewares work together to manage stateful user sessions and associate an identity with incoming requests, providing a robust foundation for traditional, cookie-based authentication.
- [**argon2**](https://docs.rs/argon2/latest/argon2/):
  - **Role:** Industry-Standard Password Hashing.
  - **Description:** A crate for securely hashing passwords using the Argon2 algorithm, the winner of the Password Hashing Competition, ensuring that user credentials are protected.

---

### **Development Workflow & Quality**

A cutting-edge Rust development environment emphasizing speed, correctness, and an efficient developer experience.

- [**cargo**](https://doc.rust-lang.org/cargo/):
  - **Role:** All-in-One Project & Package Manager.
  - **Description:** The official build tool and package manager for Rust. Cargo handles dependency management, compilation, testing, publishing, and more, serving as the cornerstone of the development workflow.
- [**Trunk**](https://trunkrs.dev/):
  - **Role:** WASM Web Application Bundler.
  - **Description:** The recommended tool for building and packaging Yew applications. Trunk simplifies the development workflow by managing your `index.html` file, handling asset bundling (CSS, images), and providing a live-reloading development server.
- [**clippy**](https://doc.rust-lang.org/clippy/):
  - **Role:** Blazing-Fast Rust Linter.
  - **Description:** An official collection of lints that catches common mistakes and improves your Rust code, ensuring it is idiomatic, performant, and correct.
- [**rustfmt**](https://rust-lang.github.io/rustfmt/):
  - **Role:** Code Formatter.
  - **Description:** A tool for automatically formatting Rust code to a community-agreed-upon style, ensuring consistency across the entire codebase.
- [**rstest**](https://docs.rs/rstest/latest/rstest/):
  - **Role:** Fixture-Based Test Framework.
  - **Description:** Enhances Rust's built-in testing capabilities by providing fixtures and parameterized/table-based testing, making your tests cleaner, more powerful, and easier to maintain.

---

### **Configuration & Error Handling**

A robust foundation for managing application configuration and handling errors gracefully.

- [**Figment**](https://docs.rs/figment/latest/figment/):
  - **Role:** Layered Application Configuration.
  - **Description:** A powerful configuration library that can merge settings from multiple sources—such as files (TOML, JSON), environment variables, and defaults—into a single, type-safe configuration struct.
- [**anyhow**](https://docs.rs/anyhow/latest/anyhow/):
  - **Role:** Flexible Application-Level Error Handling.
  - **Description:** Provides a simple and ergonomic way to handle errors in application code. It is ideal for cases where you need to easily propagate errors up the call stack without defining custom error types for every possible failure.
- [**thiserror**](https://docs.rs/thiserror/latest/thiserror/):
  - **Role:** Granular Library-Level Error Handling.
  - **Description:** A procedural macro for creating detailed, specific error types with minimal boilerplate. It is perfect for library authors or for situations where you need to distinguish between different kinds of errors programmatically.

---

### **CLI & TUI Applications**

Extend your reach beyond the web with powerful and performant native applications for the terminal.

- [**clap**](https://docs.rs/clap/latest/clap/):
  - **Role:** Powerful Command-Line Argument Parsing.
  - **Description:** The go-to library for building feature-rich and user-friendly command-line interfaces (CLIs). Clap allows you to define arguments, flags, and subcommands with a simple declarative or builder API.
- [**Ratatui**](https://ratatui.rs/tutorials/):
  - **Role:** Rich Text-Based User Interfaces (TUIs).
  - **Description:** A library for creating complex and interactive terminal applications. Ratatui provides a rich set of widgets and a flexible layout system, making it the perfect tool for building professional TUIs.

---

### **Deployment & Observability**

A lightweight, secure, and fully self-reliant deployment architecture designed for simplicity, control, and production-grade monitoring.

- [**Alpine Linux (with a static Rust build)**](https://www.alpinelinux.org/about/):
  - **Role:** Secure & Minimalist Host OS.
  - **Description:** A security-focused and resource-efficient Linux distribution that serves as an ideal small-footprint base for a statically linked Rust binary, minimizing the attack surface of your deployment.
- [**Caddy**](https://caddyserver.com/docs/):
  - **Role:** High-Performance Reverse Proxy.
  - **Description:** A powerful web server that can serve as a reverse proxy, handle automatic TLS termination (HTTPS), and load balance requests to your Rust application. Caddy is renowned for its simplicity and security.
- [**systemd**](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html):
  - **Role:** Native Process Management.
  - **Description:** The standard init system in most modern Linux distributions. You can use simple `.service` files to manage your compiled Rust application, ensuring it runs on startup and is restarted automatically on failure.
- [**Tracing**](https://docs.rs/tracing/latest/tracing/):
  - **Role:** Application-Level Observability.
  - **Description:** A modern framework for instrumenting Rust programs to collect structured, event-based diagnostic information. Use it with `tracing-subscriber` to log events to the console or export them to observability platforms like Jaeger or Datadog for production-grade monitoring.

</details>

---

## <img src="https://github.com/dunamismax/full-stack-rust/blob/main/assets/rust-crab-solo.png" width="30" height="30"> What I Build

### Applications

- **Web Servers** - High-performance Actix Web APIs with JWT authentication
- **Frontends** - Modern Yew WebAssembly applications
- **Desktop Apps** - Cross-platform Tauri applications
- **CLI Tools** - Command-line utilities with shared business logic

### Architecture

- **Type-safe contracts** between all application layers
- **Shared libraries** for maximum code reuse
- **Production-ready** patterns with CI/CD automation
- **Cross-platform** deployment strategies

---

## <img src="https://github.com/dunamismax/full-stack-rust/blob/main/assets/rust-crab-solo.png" width="30" height="30"> Support My Work

If you find my Full Stack Rust work valuable, consider supporting continued development:

<p align="center">
  <a href="https://www.buymeacoffee.com/dunamismax" target="_blank">
    <img src="https://github.com/dunamismax/full-stack-rust/blob/main/assets/buy-me-coffee-qr.png" alt="Buy Me A Coffee QR Code" width="200"/>
  </a>
</p>

<p align="center">
  <a href="https://www.buymeacoffee.com/dunamismax" target="_blank">
    <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" />
  </a>
</p>

---

## Let's Connect

<p align="center">
  <a href="https://twitter.com/dunamismax" target="_blank"><img src="https://img.shields.io/badge/Twitter-%231DA1F2.svg?&style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter"></a>
  <a href="https://bsky.app/profile/dunamismax.bsky.social" target="_blank"><img src="https://img.shields.io/badge/Bluesky-blue?style=for-the-badge&logo=bluesky&logoColor=white" alt="Bluesky"></a>
  <a href="https://reddit.com/user/dunamismax" target="_blank"><img src="https://img.shields.io/badge/Reddit-%23FF4500.svg?&style=for-the-badge&logo=reddit&logoColor=white" alt="Reddit"></a>
  <a href="https://discord.com/users/dunamismax" target="_blank"><img src="https://img.shields.io/badge/Discord-dunamismax-7289DA.svg?style=for-the-badge&logo=discord&logoColor=white" alt="Discord"></a>
  <a href="https://signal.me/#p/+dunamismax.66" target="_blank"><img src="https://img.shields.io/badge/Signal-dunamismax.66-3A76F0.svg?style=for-the-badge&logo=signal&logoColor=white" alt="Signal"></a>
</p>

---

<p align="center">
  <img src="https://github.com/dunamismax/full-stack-rust/blob/main/assets/rust-logo-title-wide.jpg" alt="Rust Logo" width="600"/>
</p>
