# Hi, I'm dunamismax

<p align="center">
  <a href="https://github.com/dunamismax">
    <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=24&pause=1000&color=00ADD8&center=true&vCenter=true&width=800&lines=IT+Director+%7C+Go+Developer;Creator+of+The+Go-Minimal+Stack.;My+Blueprint:+Go,+Chi,+SQLite,+htmx;Maximum+Performance.+Minimal+Footprint.;Check+out+my+reference+implementation+below!" alt="Typing SVG" />
  </a>
p>

I'm an IT Director with over 12 years of experience, now passionately focused on Go. My development philosophy is embodied in **The Go-Minimal Stack**, an original full-stack architecture I created for building applications with ultimate speed, simplicity, and a tiny resource footprint.

I believe in creating fast, scalable backends that compile to a single binary and deliver dynamic user experiences with minimal frontend complexity. All my development is done on **macOS** and deployed to self-hosted **Linux (Ubuntu)** servers.

---

### My GitHub Activity

<p align="center">
  <a href="https://github.com/dunamismax">
    <img src="https://github-readme-stats.vercel.app/api?username=dunamismax&show_icons=true&theme=dracula&include_all_commits=true&count_private=true" alt="dunamismax's GitHub stats" />
  </a>
</p>
<p align="center">
    <img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExYmNjYm9rdjgyMWx0OGdieGRobW94NW9xcWNzM2lnYmhpbmw2c2JuZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/gG9fVWJdN41NeiHhzk/giphy.gif" alt="Snake GIF" />
</p>

---

### My Go Toolkit

My toolkit is a reflection of the stack I created: focused on performance, simplicity, and a superior developer experience with Go at the core.

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=go,sqlite,htmx,docker,caddy,linux,ubuntu" />
  </a>
p>

<details>
<summary><h3>The Go-Minimal Stack (Click to Expand)</h3></summary>

**The Go-Minimal Stack** is my personal, opinionated blueprint for building high-performance, minimalist full-stack solutions. I designed it for ultimate speed and simplicity by combining a powerful Go backend with a featherlight, framework-free frontend. It's the ideal architecture for projects where performance, maintainability, and a small resource footprint are paramount.

---

#### ## Frontend

The frontend provides a responsive user experience with zero frameworks or build tools. What you write is what the browser runs.

- [**Directly Served Static Assets (HTML, CSS, JS)**](https://developer.mozilla.org/en-US/docs/Web/HTML)
  - **Role:** Structure, Styling, and Behavior.
  - **Description:** This stack deliberately omits any frontend build step. The `index.html`, a handwritten `style.css`, and a vanilla `script.js` are served directly by the web server. This "no-build" approach represents the pinnacle of simplicity, eliminating an entire class of tools and configuration.
- [**htmx**](https://htmx.org/docs/)
  - **Role:** Dynamic Interactivity.
  - **Description:** htmx extends HTML with attributes for modern AJAX requests directly from the markup. Instead of writing complex JavaScript, you use simple attributes like `hx-get` to make requests. The backend responds with HTML fragments, which htmx swaps into the DOM, enabling dynamic experiences without full-page reloads or frontend state management.

---

#### ## Backend

The backend is written entirely in Go, creating a fast, scalable, and secure web service.

- [**Go**](https://go.dev/doc/)
  - **Role:** Backend Language.
  - **Description:** Go is a statically typed, compiled language renowned for its performance, concurrency, and simplicity. Its ability to compile to a single, dependency-free binary makes it trivial to package inside a minimal Docker container for simple and secure deployment.
- [**Chi**](https://go-chi.io)
  - **Role:** HTTP Routing.
  - **Description:** Instead of relying only on the verbose standard library, Chi provides a lightweight, idiomatic router that simplifies handling URL parameters, middleware, and route grouping. It's built on the standard `net/http` package, offering a major developer experience boost with negligible performance overhead.
- [**sqlc**](https://docs.sqlc.dev/)
  - **Role:** Type-Safe Data Access.
  - **Description:** sqlc builds upon Go's built-in `database/sql` package. You write raw SQL queries in `.sql` files, and sqlc generates type-safe, boilerplate-free Go code to execute them. This provides the performance and control of raw SQL while eliminating common errors from manual data scanning.
- [**Standard Library (`os` & `flag`)**](https://pkg.go.dev/os)
  - **Role:** Configuration Management.
  - **Description:** Configuration is handled using Go's standard library to read environment variables (`os.Getenv`) and parse command-line options (`flag`). This aligns with the 12-Factor App methodology, ensuring the application is portable and configurable through its environment.

---

#### ## Database

The stack uses a simple, file-based database coupled with a robust tool for managing its schema.

- [**SQLite**](https://www.sqlite.org/docs.html)
  - **Role:** Database Engine.
  - **Description:** SQLite is a self-contained, serverless SQL database engine. It runs within the application process and stores the entire database in a single file on disk, eliminating the need for a separate server. Its speed and simplicity are perfect for self-hosting.
- [**golang-migrate/migrate**](https://github.com/golang-migrate/migrate)
  - **Role:** Database Schema Migrations.
  - **Description:** This tool provides a standardized, battle-tested way to handle database migrations. It uses versioned `.sql` files for both up and down migrations, ensuring the database schema can evolve safely and predictably. It can be run as a CLI tool during deployment or used as a library within the Go application on startup.

---

#### ## Development

Development tooling is focused on providing a rapid and efficient feedback loop.

- [**Air**](https://github.com/cosmtrek/air)
  - **Role:** Live Reloading.
  - **Description:** Air is a development-only utility that watches for changes in Go source code and static files (HTML, CSS). Upon saving a file, it automatically recompiles and restarts the server, providing instant feedback and dramatically accelerating the development cycle. It is not included in the final production build.

---

#### ## Deployment & Hosting

This stack is designed for straightforward, secure, and containerized self-hosting with the smallest possible footprint.

- [**Docker**](https://docs.docker.com/)
  - **Role:** Containerization.
  - **Description:** Docker packages the entire compiled Go application and all static assets into a standardized container. A multi-stage `Dockerfile` creates a minimal final image, ensuring a tiny and secure result for deployment.
- [**Caddy**](https://caddyserver.com/docs/)
  - **Role:** Web Server & Reverse Proxy.
  - **Description:** Caddy is a modern web server with automatic HTTPS. It serves the static frontend assets and acts as a secure reverse proxy, forwarding all dynamic requests to the Go application's container. Its simple configuration and automated TLS management make hosting effortless.
- [**Alpine Linux**](https://www.alpinelinux.org/about/)
  - **Role:** Host OS & Container Base.
  - **Description:** Alpine Linux is a security-oriented, lightweight Linux distribution. Its minimalism makes it the ideal base for the application's Docker container and the host operating system, minimizing resource usage and attack surface.

---

#### ## CLI Apps

For building powerful and interactive command-line applications, from simple tools to rich Text User Interfaces (TUIs).

- [**Bubble Tea**](https://github.com/charmbracelet/bubbletea)
  - **Role:** Interactive TUI (Text User Interface) Framework.
  - **Description:** For applications requiring a rich, interactive terminal experience, Bubble Tea is the premier choice. Based on the functional paradigm of The Elm Architecture, it provides a stateful and delightful way to build complex TUIs. It is part of the "Charm" ecosystem, which includes `bubbles` for pre-built components and `lipgloss` for powerful styling.

</details>

---

### My Current Focus: The Go-Minimal Reference Implementation

My **Go** monorepo serves as the official reference implementation for **The Go-Minimal Stack**. It is the central hub where I put my architectural philosophy into practice, creating a living testament to the power and elegance of this approach.

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Go_Logo_Blue.svg/1920px-Go_Logo_Blue.svg.png" alt="The Go programming language logo." width="100"/>
</p>

<p align="center">
  <a href="https://github.com/dunamismax/go">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=dunamismax&repo=go&theme=dracula&show_owner=true" alt="Reference Implementation for The Go-Minimal Stack" />
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
    <img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExb2doc3ZjMjRkb3JpeGJ6dzF2N3d5dXRnaWNrOTlzZXVnMncwY2F3NSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/g79am6uuZJKSc/giphy.gif" alt="Moss IT Crowd Fire" />
</p>
