<p align="center">
  <img src="https://github.com/dunamismax/full-stack-rust/blob/main/assets/rust-logo.png" alt="Full Stack Rust logo." width="150"/>
</p>

<p align="center">
  <a href="https://github.com/dunamismax/full-stack-rust">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=24&pause=1000&color=CE422B&center=true&vCenter=true&width=800&lines=IT+Director+%7C+Rust+Developer;Creator+of+Full+Stack+Rust;Actix+Web+%2B+Yew+%2B+SeaORM;Zero+JavaScript%2C+Maximum+Performance;Clone%2C+Configure%2C+and+Deploy!" alt="Typing SVG" />
  </a>
</p>

With over a decade of IT experience, I specialize in building blazing-fast, memory-safe, and maintainable applications with Rust. I have created the **Full Stack Rust** monorepo - a production-grade reference implementation designed for maximum performance, type safety, and unified development across the entire technology stack.

The **[Full Stack Rust](https://github.com/dunamismax/full-stack-rust)** monorepo represents the zenith of unified development: a complete, self-contained stack that leverages Rust everywhere from WebAssembly frontends to high-performance backends, desktop applications, and command-line tools.

This repository serves as both a comprehensive reference implementation and a ready-to-clone template, featuring modern Rust development patterns with Cargo workspaces, shared libraries, and automated CI/CD workflows.

---

### My Featured Project

This repository is the official reference implementation for Full Stack Rust development. It's a living project that serves as a powerful, real-world template for building robust applications with Rust across the entire technology stack.

<p align="center">
  <a href="https://github.com/dunamismax/full-stack-rust">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=dunamismax&repo=full-stack-rust&theme=dracula&show_owner=true" alt="full-stack-rust Repository" />
  </a>
</p>

---

### The Ultimate Workflow: Cargo Workspaces

One of the standout features of the Full Stack Rust stack is the **Cargo workspace architecture**. This isn't just a monorepo; it's a complete, unified development environment that manages shared dependencies, enforces consistency, and enables maximum code reuse across applications.

**Why is it so powerful?**

- **Unified Dependencies:** Centralized version management ensures consistency across all applications and libraries.
- **Code Reuse:** Shared crates eliminate duplication between frontend, backend, desktop, and CLI applications.
- **Type Safety:** Shared API contracts prevent frontend/backend type mismatches at compile time.
- **Performance:** Zero-cost abstractions and memory safety without garbage collection overhead.

With simple commands like `cargo run -p server` or `cargo tauri dev -p desktop`, you can instantly start any application in the stack. It's designed to make you productive from the very first minute.

---

### My Rust Toolkit

My toolkit reflects the Full Stack Rust philosophy: a unified language approach that maximizes performance and safety while maintaining developer productivity across the entire application stack.

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=rust,wasm,actix,sqlite,tauri,html,css,linux,ubuntu" />
  </a>
</p>

<details>
<summary><h3>The Full Stack Rust Technology Stack - Click to Expand</h3></summary>

# **The Full Stack Rust Technology Stack**

---

This stack is engineered for maximum performance, type safety, and unified development experience. It is for developers who want to leverage Rust's power across the entire application stack with minimal friction and maximum code reuse.

---

### **Frontend: WebAssembly-Powered, Component-Based UI**

This frontend architecture leverages WebAssembly (WASM) to run native Rust code directly in the browser, delivering rich, interactive user experiences with near-native performance.

- [**Yew**](https://yew.rs/docs/getting-started)
  - **Role:** Component-Based Frontend Framework.
  - **Description:** Yew is a modern Rust framework for creating multi-threaded front-end web apps using WebAssembly. It features a component-based model and an `html!` macro similar to JSX, making it familiar for developers with React experience.
- [**Stylist**](https://docs.rs/stylist/latest/stylist/)
  - **Role:** CSS-in-Rust Styling.
  - **Description:** Stylist provides a type-safe, component-scoped styling solution for Rust-based WebAssembly applications. It integrates directly with Yew and allows you to write CSS within your components for co-located and maintainable styles.
- [**Trunk**](https://trunkrs.dev/)
  - **Role:** WASM Web Application Bundler.
  - **Description:** The recommended tool for building and packaging Yew applications. Trunk simplifies the development workflow by managing your `index.html` file, handling asset bundling, and providing a live-reloading development server.
- [**Gloo**](https://docs.rs/gloo/)
  - **Role:** Modular Toolkit for Rust and WebAssembly.
  - **Description:** A collection of high-level idiomatic Rust libraries for interacting with Web APIs, providing everything from HTTP requests to local storage management.

---

### **Backend: High-Performance & Asynchronous**

This backend foundation is optimized for speed, memory safety, and high concurrency, built on Rust's powerful asynchronous ecosystem.

- [**Actix Web**](https://actix.rs/docs/)
  - **Role:** Powerful & Pragmatic Web Framework.
  - **Description:** A high-performance framework for building APIs and web services. Built on the actor model, Actix Web is capable of handling a massive number of concurrent connections with minimal resource usage.
- [**SeaORM**](https://www.sea-ql.org/SeaORM/docs/internal-architecture/architecture)
  - **Role:** Relational ORM.
  - **Description:** A dynamic and flexible Object-Relational Mapper that helps you work with databases in an idiomatic Rust fashion. It reduces boilerplate and prevents common errors by mapping database tables to Rust structs.
- [**Tokio**](https://tokio.rs/tokio/tutorial)
  - **Role:** Asynchronous Runtime.
  - **Description:** Tokio is the de-facto standard for writing asynchronous applications in Rust. It provides the non-blocking I/O platform, task scheduler, and utilities that power the entire backend.
- [**Serde**](https://serde.rs/)
  - **Role:** Robust Data Serialization & Deserialization.
  - **Description:** A powerful and generic framework for converting Rust data structures to and from formats like JSON, BSON, and more. Essential for handling data in any modern web application.

---

### **Desktop: Cross-Platform Native Applications**

Extend your reach beyond the web with powerful and secure native applications that share the same codebase.

- [**Tauri**](https://tauri.app/v1/guides/)
  - **Role:** Cross-Platform Application Toolkit.
  - **Description:** Tauri packages your Yew web frontend into a lightweight, secure, and fast desktop application. It provides the native shell for your UI, enabling access to system resources and creating installers for Windows, macOS, and Linux.

---

### **CLI: Powerful Command-Line Tools**

Build feature-rich and user-friendly command-line interfaces with the same shared business logic.

- [**Clap**](https://docs.rs/clap/latest/clap/)
  - **Role:** Powerful Command-Line Argument Parsing.
  - **Description:** The go-to library for building feature-rich and user-friendly command-line interfaces (CLIs). Clap allows you to define arguments, flags, and subcommands with a simple declarative or builder API.

---

### **Authentication & Security**

A robust and explicit approach to security, providing powerful tools to control authentication and authorization flows.

- [**Argon2**](https://docs.rs/argon2/latest/argon2/)
  - **Role:** Industry-Standard Password Hashing.
  - **Description:** A crate for securely hashing passwords using the Argon2 algorithm, the winner of the Password Hashing Competition, ensuring that user credentials are protected.
- [**JSON Web Tokens**](https://docs.rs/jsonwebtoken/latest/jsonwebtoken/)
  - **Role:** Stateless JWT Authentication.
  - **Description:** A crate for creating and verifying JSON Web Tokens (JWTs), the standard for implementing stateless authentication in modern APIs.
- [**Actix Web Grants**](https://docs.rs/actix-web-grants/latest/actix_web_grants/)
  - **Role:** Flexible Authorization for Actix Web.
  - **Description:** Provides a flexible authorization layer to protect endpoints based on user roles and permissions, integrating seamlessly with various authentication schemes.

---

### **Configuration & Error Handling**

A robust foundation for managing application configuration and handling errors gracefully.

- [**Figment**](https://docs.rs/figment/latest/figment/)
  - **Role:** Layered Application Configuration.
  - **Description:** A powerful configuration library that can merge settings from multiple sources—such as files (TOML, JSON), environment variables, and defaults—into a single, type-safe configuration struct.
- [**Anyhow**](https://docs.rs/anyhow/latest/anyhow/)
  - **Role:** Flexible Application-Level Error Handling.
  - **Description:** Provides a simple and ergonomic way to handle errors in application code. Ideal for cases where you need to easily propagate errors up the call stack without defining custom error types.
- [**Thiserror**](https://docs.rs/thiserror/latest/thiserror/)
  - **Role:** Granular Library-Level Error Handling.
  - **Description:** A procedural macro for creating detailed, specific error types with minimal boilerplate. Perfect for library authors or situations where you need to distinguish between different kinds of errors programmatically.

---

### **Development Workflow & Quality**

A cutting-edge Rust development environment emphasizing speed, correctness, and an efficient developer experience.

- [**Cargo**](https://doc.rust-lang.org/cargo/)
  - **Role:** All-in-One Project & Package Manager.
  - **Description:** The official build tool and package manager for Rust. Cargo handles dependency management, compilation, testing, publishing, and more, serving as the cornerstone of the development workflow.
- [**Clippy**](https://doc.rust-lang.org/clippy/)
  - **Role:** Blazing-Fast Rust Linter.
  - **Description:** An official collection of lints that catches common mistakes and improves your Rust code, ensuring it is idiomatic, performant, and correct.
- [**Rustfmt**](https://rust-lang.github.io/rustfmt/)
  - **Role:** Code Formatter.
  - **Description:** A tool for automatically formatting Rust code to a community-agreed-upon style, ensuring consistency across the entire codebase.
- [**Tracing**](https://docs.rs/tracing/latest/tracing/)
  - **Role:** Application-Level Observability.
  - **Description:** A modern framework for instrumenting Rust programs to collect structured, event-based diagnostic information for production-grade monitoring.

---

### **Deployment & Observability**

A lightweight, secure, and fully self-reliant deployment architecture designed for simplicity, control, and production-grade monitoring.

- [**Alpine Linux (with static Rust builds)**](https://www.alpinelinux.org/about/)
  - **Role:** Secure & Minimalist Host OS.
  - **Description:** A security-focused and resource-efficient Linux distribution that serves as an ideal small-footprint base for statically linked Rust binaries, minimizing the attack surface.
- [**Systemd**](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html)
  - **Role:** Native Process Management.
  - **Description:** The standard init system in most modern Linux distributions. Use simple `.service` files to manage your Rust applications, ensuring they run on startup and restart automatically on failure.

</details>

---

### Support My Work

If you find my work on the Full Stack Rust stack valuable, please consider supporting me. It helps me dedicate more time to creating and maintaining high-quality open-source projects.

<p align="center">
  <a href="https://www.buymeacoffee.com/dunamismax" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
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
