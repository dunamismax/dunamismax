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

<details>
<summary><strong>Click to expand: Complete Technology Stack</strong></summary>

### Frontend: Reactive, Zero-JavaScript, WebAssembly-Powered

- **[Yew 0.21](https://yew.rs/)** - Component-based frontend framework with WebAssembly
- **[Tailwind CSS](https://tailwindcss.com/)** - Utility-first styling via CDN
- **[Trunk](https://trunkrs.dev/)** - WASM web application bundler

### Backend: High-Performance & Production-Ready

- **[Actix Web 4.11](https://actix.rs/)** - High-performance async web framework
- **[Tokio](https://tokio.rs/)** - Asynchronous runtime
- **[Serde](https://serde.rs/)** - Data serialization framework

### Database & Persistence

- **[PostgreSQL 15+](https://www.postgresql.org/)** - Production-grade relational database
- **[SeaORM 1.1](https://www.sea-ql.org/SeaORM/)** - Async ORM for Rust

### Security & Authentication

- **[argon2](https://docs.rs/argon2/)** - Password hashing
- **[jsonwebtoken](https://docs.rs/jsonwebtoken/)** - JWT authentication
- **[actix-web-grants](https://docs.rs/actix-web-grants/)** - Authorization middleware

### Development & Quality

- **[Figment](https://docs.rs/figment/)** - Layered configuration
- **[anyhow & thiserror](https://docs.rs/anyhow/)** - Error handling
- **Comprehensive CI/CD** - Format checking, linting, testing, security auditing

### Deployment & Observability

- **Docker & Kubernetes** - Containerized deployment
- **Alpine Linux** - Minimal, secure base images
- **Tracing** - Structured logging and observability

</details>

---

## What I Build

### Applications

- **Web APIs** - High-performance Actix Web servers with JWT authentication
- **WebAssembly Frontends** - Modern Yew applications with Tailwind CSS
- **Production Infrastructure** - PostgreSQL databases with SeaORM
- **CI/CD Pipelines** - Automated testing, security scanning, and deployment

### Architecture Patterns

- **Type-safe contracts** between all application layers
- **Shared libraries** for maximum code reuse across the stack
- **Production-ready** patterns with comprehensive testing
- **Security-first** design with modern authentication practices

---

## Key Features Demonstrated

### Complete Authentication System

- User registration and login with validation
- JWT-based stateless authentication
- Secure Argon2 password hashing with salt
- Protected routes with middleware authorization
- Automatic database table creation

### Modern Development Workflow

- Live reload for frontend development
- Hot reloading for backend changes
- Comprehensive error handling
- Security headers and input validation
- Structured logging with tracing

### Production-Grade Infrastructure

- PostgreSQL database integration
- Docker and Kubernetes deployment
- Comprehensive CI/CD pipeline
- Cross-platform builds and testing
- Security auditing with cargo-audit

---

## Quick Start Example

```bash
# Clone the repository
git clone https://github.com/dunamismax/full-stack-rust.git
cd full-stack-rust

# Setup PostgreSQL database
createdb fullstackrust

# Start backend server (Terminal 1)
cargo run -p server

# Start frontend dev server (Terminal 2)
cd ui/webapp && trunk serve

# Visit http://127.0.0.1:8080
```

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
  <img src="https://github.com/dunamismax/full-stack-rust/blob/main/assets/rust-logo-title-wide.jpg" alt="Rust Logo" width="600"/>
</p>

<p align="center">
  <strong>Building the future with Rust - one monorepo at a time</strong><br>
  <sub>Zero JavaScript, Maximum Performance, Production Ready</sub>
</p>
