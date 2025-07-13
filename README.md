<p align="center">
  <img src="https://github.com/dunamismax/espresso-driven-development/blob/main/shared/static/images/python-coffee.png" alt="Espresso-Driven Development logo." width="150"/>
</p>

<p align="center">
  <a href="https://github.com/dunamismax/espresso-driven-development">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=24&pause=1000&color=8B4513&center=true&vCenter=true&width=800&lines=IT+Director+%7C+Python+Developer;Creator+of+Espresso-Driven+Development;FastAPI+%2B+htmx+%2B+SQLAlchemy+Core;Zero+JavaScript%2C+Maximum+Velocity;Clone%2C+Configure%2C+and+Deploy!" alt="Typing SVG" />
  </a>
</p>

With over a decade of IT experience, I specialize in building fast, maintainable, and powerful web applications with Python. I have created the **Espresso-Driven Development** stack - a radically simple Python hypermedia architecture designed for maximum development velocity and minimalist design.

The **[Espresso-Driven Development](https://github.com/dunamismax/espresso-driven-development)** monorepo represents the zenith of Python web development simplicity: a self-contained, hypermedia-driven stack that eliminates JavaScript build steps while delivering rich, interactive user experiences through the power of FastAPI, htmx, and SQLAlchemy Core.

This repository serves as both a complete reference implementation and a ready-to-clone template, featuring a powerful `justfile` that orchestrates the entire development lifecycle with simple commands like `just blog` or `just dashboard`.

---

### My Featured Project

This repository is the official reference implementation for the Espresso-Driven Development stack. It's a living project that serves as a powerful, real-world template for building robust Python web applications with zero JavaScript complexity.

<p align="center">
  <a href="https://github.com/dunamismax/espresso-driven-development">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=dunamismax&repo=espresso-driven-development&theme=dracula&show_owner=true" alt="espresso-driven-development Repository" />
  </a>
</p>

---

<p align="center">
  <img src="https://github.com/dunamismax/espresso-driven-development/blob/main/shared/static/images/python-coffee.png" alt="Python Coffee." width="150"/>
</p>

### The Ultimate Workflow: The `justfile`

One of the standout features of the Espresso-Driven Development stack is the **`justfile`**. This isn't just a task runner; it's a complete, cross-platform command orchestrator that manages the entire development lifecycle. It provides a seamless experience without complex build processes.

**Why is it so great?**

- **Simplicity:** Manage complex workflows with simple commands like `just blog` or `just dashboard`.
- **Consistency:** Ensures every developer on a project uses the exact same commands for running, testing, and quality checks.
- **Speed:** Written for maximum velocity - get from idea to running application in seconds.

With a single command, you can start interactive web applications, run comprehensive tests, and format your entire codebase. It's designed to make you productive from the very first minute.

---

### My Python Toolkit

My toolkit reflects the Espresso-Driven Development philosophy: a hypermedia-first approach that maximizes development velocity while maintaining the power and elegance of Python.

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=python,fastapi,sqlite,tailwind,html,css,linux,ubuntu" />
  </a>
</p>

<details open>
<summary><h3>The Espresso-Driven Development Stack (Click to Expand)</h3></summary>

---

This stack is engineered for the absolute zenith of development speed and minimalist design. It is for developers who want to move from idea to a running application with the fewest possible moving parts. By eliminating the JavaScript ecosystem and stripping away layers of abstraction, this stack uses a powerful, Python-centric hypermedia approach. The result is a radically simple, cohesive, and blazing-fast stack that is trivial to deploy and maintain.

---

### **Frontend: Hypermedia-Powered, JavaScript-Free**

This frontend architecture is built on the principle of "HTML over the wire." It delivers rich, interactive user experiences without client-side JavaScript by having the server handle all logic and rendering, resulting in an incredibly simple and fast development loop.

- [**htmx**](https://htmx.org/docs/)
  - **Role:** Declarative Hypermedia Interactivity.
  - **Description:** The core of the frontend. htmx supercharges HTML with simple attributes, enabling you to trigger server requests and swap page content dynamically. It provides the feel of a modern SPA without writing a single line of JavaScript.
- [**Hyperscript**](https://hyperscript.org/docs/)
  - **Role:** Intuitive, Inline Event Handling.
  - **Description:** A perfect companion to htmx for handling trivial client-side behaviors. Its natural language syntax allows you to add simple interactivity (like toggling a CSS class) directly in your HTML, maintaining perfect locality of behavior.
- [**Jinja Templates**](https://jinja.palletsprojects.com/en/3.1.x/)
  - **Role:** Powerful Server-Side HTML Rendering.
  - **Description:** The definitive templating engine for Python. Jinja constructs the HTML on the server, seamlessly weaving your application's data into templates that are sent directly to the browser as complete, ready-to-display content.
- [**Tailwind CSS (via Play CDN)**](https://tailwindcss.com/docs/installation/play-cdn)
  - **Role:** Build-Free, Utility-First Styling.
  - **Description:** Provides a complete, utility-first CSS framework for crafting bespoke designs with maximum speed. The Play CDN enables access to the full power of Tailwind directly in the browser, completely removing the need for `npm` or any build steps.

---

### **Backend: High-Performance & Explicit**

This backend foundation is optimized for performance, developer ergonomics, and direct control, with a strong emphasis on Python's type-safety features.

- [**FastAPI**](https://fastapi.tiangolo.com/)
  - **Role:** Modern Python Web Framework.
  - **Description:** The high-performance engine for the entire application. It serves the hypermedia-driven frontend and provides a robust, type-safe foundation for building any necessary APIs with automatic data validation and documentation.
- [**SQLAlchemy Core**](https://docs.sqlalchemy.org/en/20/core/)
  - **Role:** Powerful SQL Expression Toolkit.
  - **Description:** Provides the full power of SQL through a Pythonic expression language. This gives you direct, granular control over your database interactions without the indirection of a traditional ORM, promoting clear and optimized queries.
- [**Uvicorn**](https://www.uvicorn.org/)
  - **Role:** Lightning-Fast ASGI Server.
  - **Description:** A high-performance server that acts as the production-ready engine for your FastAPI application, serving requests with incredible speed and efficiency.
- [**Pydantic V2**](https://docs.pydantic.dev/latest/)
  - **Role:** Bulletproof Data Validation.
  - **Description:** Guarantees data integrity throughout your application. It uses Python type hints to validate, parse, and serialize data, catching errors early and integrating seamlessly with FastAPI.

---

### **Data & Background Processing: Lean & Self-Contained**

This data layer is designed for ultimate simplicity, with zero external service dependencies.

- [**SQLite**](https://www.sqlite.org/docs.html)
  - **Role:** Zero-Configuration Embedded Database.
  - **Description:** A self-contained, file-based SQL database that requires no setup or administration. It is the gold standard for rapid prototyping, embedded applications, and simple, self-hosted deployments.
- [**FastAPI BackgroundTasks**](https://fastapi.tiangolo.com/tutorial/background-tasks/)
  - **Role:** Simple, In-Process Task Execution.
  - **Description:** For fire-and-forget operations like sending emails or notifications. These tasks run in the background after a response is sent, requiring zero external dependencies, message brokers, or worker processes.

---

### **Development Workflow: Modern & Fast**

A cutting-edge Python development environment emphasizing speed, consistency, and a delightful developer experience.

- [**uv**](https://docs.astral.sh/uv/)
  - **Role:** All-in-One Python Project & Package Manager.
  - **Description:** An extremely fast tool written in Rust that replaces pip and venv. It provides a 10-100x speedup for dependency management, making your development workflow significantly faster.
- [**Ruff**](https://docs.astral.sh/ruff/)
  - **Role:** Blazing-Fast Python Linter & Formatter.
  - **Description:** Combines the functionality of dozens of tools like Flake8, isort, and Black into one Rust-powered binary, providing near-instantaneous feedback and code formatting.
- [**mypy**](https://mypy.readthedocs.io/en/stable/)
  - **Role:** Static Type Checker for Error Prevention.
  - **Description:** The standard static type checker for Python. It analyzes your code to catch type-related errors before they happen at runtime, ensuring correctness and improving code quality.
- [**just**](https://github.com/casey/just)
  - **Role:** A Modern Command Runner.
  - **Description:** A simple and effective tool for saving and running project-specific commands. It acts as a modern, cross-platform alternative to `make` for common tasks like starting the server or running tests.

---

### **Authentication & Security: Lean & Controlled**

A direct and transparent approach to security, giving you full control over the authentication flow using the framework's own robust tools.

- [**FastAPI Middleware & Dependencies**](https://fastapi.tiangolo.com/tutorial/middleware/)
  - **Role:** Custom Session-Based Authentication.
  - **Description:** Build a lean and transparent authentication system using FastAPI's own tools. A middleware can create a secure, cookie-based session, and a dependency can protect specific routes, giving you full control over the user flow.
- [**passlib[bcrypt]**](https://passlib.readthedocs.io/en/stable/)
  - **Role:** Industry-Standard Password Hashing.
  - **Description:** A crucial library for protecting user credentials. It provides a simple and secure way to hash and verify passwords using the proven and adaptive bcrypt algorithm.

---

### **Deployment & Operations: Minimalist & Self-Hosted**

A lightweight, secure, and fully self-reliant deployment architecture designed for ultimate control and simplicity.

- [**Alpine Linux**](https://docs.alpinelinux.org/user-handbook/overview/)
  - **Role:** Secure & Minimalist Host OS.
  - **Description:** A security-focused and resource-efficient Linux distribution that serves as the perfect small-footprint base for running your application on a VPS.
- [**Caddy**](https://caddyserver.com/docs/)
  - **Role:** Zero-Effort HTTPS Web Server.
  - **Description:** A powerful web server that provides automatic, hands-free HTTPS certificate provisioning and renewal. It serves as a secure reverse proxy, directing traffic to your application with minimal configuration.
- [**systemd**](https://www.freedesktop.org/software/systemd/man/systemd.service.html)
  - **Role:** Native Process Management.
  - **Description:** The init system built into most modern Linux distributions. Use simple `.service` files to manage your Uvicorn process, ensuring it runs on startup and restarts automatically without adding third-party dependencies.
- [**Python `logging` Module**](https://docs.python.org/3/library/logging.html)
  - **Role:** Dependency-Free Application Logging.
  - **Description:** The standard Python library for emitting event logs from your application. It can be configured to write to standard output or files, providing a simple, robust, and entirely self-contained logging solution.

</details>

---

### Support My Work

If you find my work on the Espresso-Driven Development stack valuable, please consider supporting me. It helps me dedicate more time to creating and maintaining high-quality open-source projects.

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

<p align="center">
    <img src="https://github.com/dunamismax/espresso-driven-development/blob/main/shared/static/images/python-coffee.png" alt="Espresso-Driven Development" width="100"/>
</p>
