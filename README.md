<p align="center">
  <img src="https://github.com/dunamismax/full-stack-rust/blob/main/assets/rust-wallpaper-crab-new.png" alt="dunamismax - Full Stack Rust Developer" width="800"/>
</p>

<p align="center">
  <a href="https://github.com/dunamismax/full-stack-rust">
    <img src="https://readme-typing-svg.demolab.com/?font=Fira+Code&size=24&pause=1000&color=CE422B&center=true&vCenter=true&width=800&lines=IT+Director+%7C+Rust+Developer;Creator+of+Full+Stack+Rust;Yew+%2B+Actix+Web+%2B+PostgreSQL;Zero+JavaScript%2C+Maximum+Performance;Clone%2C+Configure%2C+and+Deploy!" alt="Typing SVG" />
  </a>
</p>

<p align="center">
  <a href="https://github.com/dunamismax/full-stack-rust/actions/workflows/ci.yml"><img src="https://github.com/dunamismax/full-stack-rust/workflows/CI/badge.svg" alt="CI Status"></a>
  <a href="https://www.rust-lang.org/"><img src="https://img.shields.io/badge/Rust-1.70+-CE422B.svg?logo=rust" alt="Rust Version"></a>
  <a href="https://yew.rs/"><img src="https://img.shields.io/badge/Yew-0.21-green.svg?logo=rust" alt="Yew Version"></a>
  <a href="https://actix.rs/"><img src="https://img.shields.io/badge/Actix_Web-4.11-blue.svg?logo=rust" alt="Actix Web Version"></a>
  <a href="https://www.postgresql.org/"><img src="https://img.shields.io/badge/PostgreSQL-15+-blue.svg?logo=postgresql" alt="PostgreSQL"></a>
</p>

---

## About Me

With over a decade of IT experience, I specialize in building blazing-fast, memory-safe, and maintainable applications with Rust. I have created the **Full Stack Rust** monorepo - a production-grade reference implementation that demonstrates modern web development using Rust across the entire technology stack.

**Focus**: Building complete applications using Rust everywhere - from WebAssembly frontends to high-performance backends with PostgreSQL.

**Philosophy**:

- **Single Language Everywhere** - Rust from frontend to backend to database
- **Type-Safe Contracts** - Shared API types prevent frontend/backend drift
- **Production-Grade Security** - JWT authentication + Argon2 password hashing
- **Zero JavaScript** - Pure Rust + WebAssembly frontend with native performance

---

## Featured Project

**[Full Stack Rust](https://github.com/dunamismax/full-stack-rust)** represents the pinnacle of unified development: a complete, production-ready stack that leverages Rust everywhere from WebAssembly frontends to high-performance backends with PostgreSQL.

<p align="center">
  <a href="https://github.com/dunamismax/full-stack-rust">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=dunamismax&repo=full-stack-rust&theme=dracula&show_owner=true" alt="full-stack-rust Repository" />
  </a>
</p>

This repository serves as both a comprehensive reference implementation and a ready-to-clone template, featuring:

- **Complete Authentication System** - User registration, login, JWT tokens, protected routes
- **Modern Web Architecture** - Component-based frontend, RESTful API, type-safe contracts
- **Production-Grade Infrastructure** - PostgreSQL, error handling, security headers, CI/CD
- **Excellent Developer Experience** - Live reload, hot reloading, shared libraries

---

## The Cargo Workspace Advantage

The **Cargo workspace architecture** isn't just a monorepo; it's a complete, unified development environment that manages shared dependencies, enforces consistency, and enables maximum code reuse across applications.

**Why it's powerful**:

- **Unified Dependencies** - Centralized version management ensures consistency
- **Code Reuse** - Shared crates eliminate duplication between frontend and backend
- **Type Safety** - Shared API contracts prevent frontend/backend type mismatches at compile time
- **Performance** - Zero-cost abstractions and memory safety without garbage collection overhead

With simple commands like `cargo run -p server` or `cd ui/webapp && trunk serve`, you can instantly start any application in the stack.

---

## Tech Stack

My toolkit reflects the Full Stack Rust philosophy: a unified language approach that maximizes performance and safety while maintaining developer productivity.

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=rust,wasm,actix,postgresql,html,css,docker,linux" />
  </a>
</p>

---

<details>
<summary><strong>Click to expand: Complete Technology Stack</strong></summary>

Below is a comprehensive, full-stack technology architecture leveraging the Rust programming language. The stack is designed to facilitate the development of high-performance, scalable, and maintainable web applications. By utilizing Rust across all layers, from the WebAssembly-powered frontend to the asynchronous backend, this architecture ensures robust type safety, exceptional performance, and a unified development experience.

### **Frontend: Reactive, Buildless, & WebAssembly-Powered**

This frontend architecture runs native Rust code directly in the browser using WebAssembly (WASM), delivering rich, interactive user experiences with incredible performance. The development workflow is streamlined for simplicity by using a "buildless" approach for styling, eliminating the need for complex JavaScript tooling.

- [**Yew**](https://yew.rs/)
  - **Role:** Component-Based Frontend Framework
  - **Description:** Yew is a modern Rust framework for creating multi-threaded front-end web apps with WebAssembly. Its component-based model and `html!` macro, which is similar to JSX, provide a familiar and powerful development experience for building complex, interactive user interfaces.
- [**Tailwind CSS via Play CDN**](https://tailwindcss.com/docs/installation/play-cdn)
  - **Role:** Utility-First Styling (No Build Step)
  - **Description:** This method integrates the full power of the Tailwind CSS framework by simply adding a script tag to your `index.html`. The Play CDN dynamically scans your HTML for utility classes and generates the necessary styles in the browser. This is ideal for rapid development and projects where you want to avoid a JavaScript-based build process entirely. **Note:** The official Tailwind documentation recommends using this for development purposes; for production, it is best practice to generate and use a static CSS file.
- [**Trunk**](https://trunkrs.dev/)
  - **Role:** WASM Web Application Bundler
  - **Description:** Trunk is the essential build tool and development server for Yew applications. It automates the process of managing your `index.html` file, bundling WASM and other assets, and provides a live-reloading server, creating a seamless and efficient development cycle.
- [**Yew Components**](https://github.com/wiseaidev/yew-components)
  - **Role:** Pre-built UI Components
  - **Description:** A versatile collection of reusable components designed for Yew, including ready-to-use forms for login, registration, and contact. These components come with styles for various CSS frameworks, including Tailwind CSS, greatly accelerating UI development.
- [**Material Yew**](https://github.com/yewstack/material-yew)
  - **Role:** Material Design Components
  - **Description:** This library provides a complete set of Yew components that wrap Material Web Components, allowing you to easily and faithfully implement Google's popular Material Design system in your Rust-based web application.

### **Backend: Asynchronous & Scalable**

The foundation of this stack is engineered for exceptional speed, robust memory safety, and massive concurrency, harnessing Rust's cutting-edge asynchronous ecosystem.

- [**Tokio**](https://tokio.rs/tokio/tutorial)
  - **Role:** Asynchronous Runtime
  - **Description:** As the de-facto standard for asynchronous applications in Rust, Tokio provides the essential non-blocking I/O platform, task scheduler, and utilities that power the entire backend. Its event-driven architecture is designed for building reliable network applications without compromising on speed.
- [**Actix Web**](https://actix.rs/docs/)
  - **Role:** High-Performance Web Framework
  - **Description:** Actix Web is a powerful and pragmatic framework for crafting APIs and web services. Renowned for its extreme speed and efficient resource management, it can handle a vast number of concurrent connections, making it ideal for demanding, high-performance backend services.
- [**Serde**](https://serde.rs/)
  - **Role:** Data Serialization & Deserialization
  - **Description:** An indispensable framework for the efficient and generic conversion of Rust data structures to and from a multitude of formats like JSON. Serde is a critical component for handling data in any modern web application, integrating seamlessly with other parts of the ecosystem.

### **Data Persistence Layer**

This data layer is architected for unwavering reliability and seamless integration with Rust, featuring a production-grade database solution.

- [**PostgreSQL**](https://www.postgresql.org/docs/)
  - **Role:** Production-Grade Relational Database
  - **Description:** A powerful, open-source object-relational database system with an unparalleled reputation for reliability, feature robustness, and performance. PostgreSQL provides a scalable and durable foundation for production applications.
- [**SeaORM**](https://www.sea-ql.org/SeaORM/docs/internal-architecture/architecture)
  - **Role:** Relational ORM
  - **Description:** A dynamic and flexible Object-Relational Mapper that enables developers to interact with databases in an idiomatic and safe Rust fashion. By mapping database tables to Rust structs, SeaORM significantly reduces boilerplate code and prevents common data-related bugs.

### **Security & Authentication**

A direct and explicit approach to security, providing robust tools to control the authentication and authorization flow in your application.

- [**argon2**](https://docs.rs/argon2/latest/argon2/)
  - **Role:** Industry-Standard Password Hashing
  - **Description:** This crate offers a secure implementation of the Argon2 algorithm, the winner of the Password Hashing Competition. It ensures that user credentials are protected with a state-of-the-art, memory-hard hashing function.
- [**jsonwebtoken**](https://docs.rs/jsonwebtoken/latest/jsonwebtoken/)
  - **Role:** Stateless JWT Authentication
  - **Description:** A crate for creating and verifying JSON Web Tokens (JWTs), the standard for implementing stateless authentication in modern APIs, offering a powerful and secure alternative to traditional session management.
- [**actix-web-grants**](https://docs.rs/actix-web-grants/latest/actix_web_grants/)
  - **Role:** Flexible Authorization for Actix Web
  - **Description:** This library provides a flexible authorization layer to protect endpoints based on user roles and permissions. It seamlessly integrates with various authentication schemes to enforce access control policies.
- [**actix-identity**](https://docs.rs/actix-identity/latest/actix_identity/) & [**actix-session**](https://docs.rs/actix-session/latest/actix_session/)
  - **Role:** Session Management and User Identity
  - **Description:** These middlewares work in tandem to manage stateful user sessions and associate an identity with incoming requests. They provide a robust foundation for traditional, cookie-based authentication.

### **Development & Quality Assurance**

A state-of-the-art Rust development environment that emphasizes speed, correctness, and an efficient developer experience.

- [**cargo**](https://doc.rust-lang.org/cargo/)
  - **Role:** Project & Package Manager
  - **Description:** The official build tool and package manager for Rust. Cargo is the cornerstone of the development workflow, expertly handling dependency management, compilation, testing, and more.
- [**rustfmt**](https://rust-lang.github.io/rustfmt/)
  - **Role:** Code Formatter
  - **Description:** A tool for automatically formatting Rust code to a community-agreed-upon style, ensuring consistency and readability across the entire codebase.
- [**clippy**](https://doc.rust-lang.org/clippy/)
  - **Role:** Rust Linter
  - **Description:** An official and extensive collection of lints that catches common mistakes and improves your Rust code. Clippy is an invaluable tool for writing code that is more idiomatic, performant, and correct.
- [**rstest**](https://docs.rs/rstest/latest/rstest/)
  - **Role:** Fixture-Based Test Framework
  - **Description:** Enhances Rust's built-in testing capabilities by providing fixtures and parameterized/table-based testing, making tests cleaner, more powerful, and easier to maintain.

### **Configuration & Error Handling**

A robust foundation for managing application configuration and handling errors gracefully and effectively.

- [**Figment**](https://docs.rs/figment/latest/figment/)
  - **Role:** Layered Application Configuration
  - **Description:** A powerful configuration library that can merge settings from multiple sources—such as files (TOML, JSON), environment variables, and defaults—into a single, type-safe configuration struct.
- [**thiserror**](https://docs.rs/thiserror/latest/thiserror/)
  - **Role:** Granular Library-Level Error Handling
  - **Description:** A procedural macro for creating detailed, specific error types with minimal boilerplate. It is perfect for situations where distinguishing between different kinds of errors programmatically is essential.
- [**anyhow**](https://docs.rs/anyhow/latest/anyhow/)
  - **Role:** Flexible Application-Level Error Handling
  - **Description:** Provides a simple and ergonomic way to handle errors in application code. It is ideal for cases where you need to easily propagate errors up the call stack without defining custom error types for every possible failure.

### **Deployment & Observability**

A modern, container-native deployment and observability architecture designed for scalability, control, and production-grade monitoring.

- [**Docker**](https://docs.docker.com/)
  - **Role:** Containerization
  - **Description:** The definitive platform for developing, shipping, and running applications in containers. Docker encapsulates the application and its dependencies into a lightweight, portable container, ensuring consistency across development, testing, and production environments.
- [**Kubernetes**](https://kubernetes.io/docs/)
  - **Role:** Container Orchestration
  - **Description:** The industry-leading open-source platform for automating the deployment, scaling, and management of containerized applications. Kubernetes orchestrates the containerized Rust application, providing high availability, resilience, and seamless scaling in production.
- [**Caddy**](https://www.notion.so/ssawyer/https.caddyserver.com/docs/)
  - **Role:** High-Performance Reverse Proxy
  - **Description:** A powerful, modern web server that can serve as a reverse proxy, handle automatic TLS termination (HTTPS), and load balance requests to your Rust application. Caddy is renowned for its simplicity, security, and automatic HTTPS capabilities.
- [**Tracing**](https://docs.rs/tracing/latest/tracing/)
  - **Role:** Application-Level Observability
  - **Description:** A modern framework for instrumenting Rust programs to collect structured, event-based diagnostic information. In conjunction with subscribers like `tracing-subscriber`, it allows for logging events and exporting them to observability platforms for production-grade monitoring and analysis.

</details>

---

## What I Build

### Applications

- **Web APIs** - High-performance Actix Web servers with JWT authentication
- **WebAssembly Frontends** - Modern Yew applications with Tailwind CSS
- **Production Infrastructure** - PostgreSQL databases with SeaORM
- **CI/CD Pipelines** - Automated testing, security scanning, and deployment

---

## Support My Work

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

**Other Ways to Support:**

- Star the [Full Stack Rust repository](https://github.com/dunamismax/full-stack-rust)
- Report bugs and suggest improvements
- Share the project with others
- Contribute code or documentation

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
  <img src="https://github.com/dunamismax/full-stack-rust/blob/main/assets/rust-logo-title-wide.jpg" alt="Rust Logo" width="300"/>
</p>

<p align="center">
  <strong>Built with ❤️ and ☕ using Rust</strong><br>
  <sub>Perfect for building the next generation of web applications</sub>
</p>
