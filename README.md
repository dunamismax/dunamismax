# Hi there, I'm dunamismax

<p align="center">
  <a href="https://github.com/dunamismax">
    <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=24&pause=1000&color=00ADD8&center=true&vCenter=true&width=600&lines=IT+Director+%7C+Golang+Developer;Building+High-Performance+Web+Services;Open-Source+%26+Self-Hosting+Advocate" alt="Typing SVG" />
  </a>
</p>

I'm an IT Director with over 15 years of experience in system administration, VoIP, and web hosting. I am now focused on mastering **Go** to build robust, elegant, and high-performance web applications, APIs, and CLI tools. My development environment is **macOS**, with a focus on deploying to self-hosted **Ubuntu** servers.

---

### My GitHub Stats

<p align="center">
  <a href="https://github.com/dunamismax">
    <img src="https://github-readme-stats.vercel.app/api?username=dunamismax&show_icons=true&theme=dracula&include_all_commits=true&count_private=true" alt="dunamismax's GitHub stats" />
  </a>
  <a href="https://github.com/dunamismax">
    <img src="https://github-readme-streak-stats.herokuapp.com/?user=dunamismax&theme=dracula" alt="dunamismax's GitHub streak stats" />
  </a>
</p>

---

### My Go Toolkit

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=go,chi,postgres,caddy,htmx,tailwind,git,github,vscode,linux,ubuntu,bash" />
  </a>
</p>

<details>
<summary><h3>My Go Tech Stack</h3></summary>

This stack is designed for modern, high-performance, and concurrent web and command-line applications, self-hosted on Ubuntu and served with Caddy. It prioritizes simplicity, performance, and a stellar developer experience through Go's powerful native tooling.

#### **Core Application & CLI**

- **Language:** [**Go**](https://go.dev/doc/) (v1.22+)
  - The application's foundation. Go is a statically typed, compiled language designed for building simple, reliable, and efficient software. Its strength lies in native concurrency and a single binary output.
- **Web Router:** [**Chi**](https://go-chi.io/) (v5.0.14) or [**Gin**](https://gin-gonic.com/docs/) (v1.10.0)
  - Unlike Python, Go's powerful `net/http` standard library handles most web server needs. A lightweight router is added for ergonomic routing, middleware, and URL parameters. **Chi** is known for being idiomatic and composable, while **Gin** is praised for high performance and a rich feature set.
- **CLI Framework:** [**Cobra**](https://cobra.dev/) (v1.8.1)
  - The de-facto standard for creating powerful and modern CLI applications in Go. It's used by major projects like Kubernetes and Hugo.
- **Database Access:** **Standard `database/sql`** + [**sqlc**](https://docs.sqlc.dev/) (v1.26.0)
  - The Go community prefers writing SQL. The standard library's `database/sql` package provides the core interface. `sqlc` generates fully type-safe, idiomatic Go code from your raw SQL queries, giving you the safety and speed of an ORM without the runtime overhead.
- **Database Driver (PostgreSQL):** [**pgx**](https://pkg.go.dev/github.com/jackc/pgx/v5) (v5.6.0)
  - A high-performance and feature-rich PostgreSQL driver for Go. It integrates perfectly with `database/sql` and `sqlc` and supports asynchronous operations natively.
- **Database Migrations:** [**Goose**](https://github.com/pressly/goose) (v3.20.0)
  - A robust, CLI-based tool for managing database schema migrations. You can write migrations in plain SQL or in Go for more complex logic.

#### **Developer Experience & Tooling**

- **Package & Environment Management:** [**Go Modules & Toolchain**](https://go.dev/doc/tool/)
  - Natively built into the language. The `go` command handles dependency management (`go get`), building (`go build`), formatting (`go fmt`), and linting (`go vet`) out of the box, providing a unified and simple experience.
- **Linter & Formatter:** [**`go fmt`**](https://pkg.go.dev/cmd/gofmt/) & [**`go vet`**](https://pkg.go.dev/cmd/vet/)
  - `go fmt` automatically formats your code to the canonical Go style, ensuring consistency across the entire ecosystem. `go vet` is a static analyzer that reports suspicious constructs and helps find bugs.
- **Configuration:** [**Viper**](https://github.com/spf13/viper) (v1.19.0)
  - A complete configuration solution for Go applications. It can handle everything from `.env` files and other formats to environment variables and remote config systems.
- **Development Server:** [**Air**](https://github.com/cosmtrek/air) (v1.52.0)
  - A live-reloading command-line tool for Go applications. It watches your files for changes and automatically rebuilds and restarts your application, just like Uvicorn's reload feature.

#### **Frontend & User Experience**

- **Client-Side Interactivity:** [**htmx**](https://htmx.org/docs/) (v2.0.0)
  - htmx is backend-agnostic and works beautifully with Go. Your Go handlers will simply serve HTML snippets in response to htmx-driven requests.
- **Templating:** **Standard `html/template`**
  - Go's built-in `html/template` package is the standard for server-side HTML rendering. It's powerful, fast, and provides automatic, context-aware escaping to protect against XSS attacks.
- **Go/htmx Integration:** **Standard Handlers**
  - No special library is needed. A standard Go HTTP handler that writes an HTML template to the `http.ResponseWriter` is all you need to integrate with htmx.
- **Forms & Validation:** [**Validator**](https://github.com/go-playground/validator) (v10.22.0)
  - The most popular library for struct and field validation based on tags. You define validation rules directly on your data structs, making your code clean and readable.
- **Client-Side Validation:** **HTML5 Validation**
  - Remains the same. Built-in browser features provide instant client-side validation and are a great first line of defense.

#### **Authentication**

- **Core Authentication:** **JWT Libraries** & **`golang.org/x/crypto/bcrypt`**
  - The Go ecosystem uses well-vetted libraries for handling JWTs, such as [`golang-jwt/jwt`](https://github.com/golang-jwt/jwt).
  - Password hashing is handled by Go's official `bcrypt` package, which is secure and easy to use.

#### **Deployment & Production**

- **Web Server / Reverse Proxy:** [**Caddy**](https://caddyserver.com/docs/) (v2)
  - Caddy remains the perfect choice. It's a production-grade, open-source web server with automatic HTTPS that will act as a reverse proxy for your compiled Go application binary.
- **Asset Management:** [**Go `embed` Package**](https://pkg.go.dev/embed)
  - Introduced in Go 1.16, the `embed` package allows you to bundle static assets like CSS, JavaScript, and images directly into your Go binary at compile time. This creates a single, self-contained executable that is incredibly easy to deploy.

</details>

---

### My Go Learning Journey

I'm documenting my entire learning journey in my Go monorepo. It is the central hub for all my applications and experiments. Follow my progress there!

<p align="center">
  <a href="https://github.com/dunamismax/go">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=dunamismax&repo=go&theme=dracula" alt="Go Monorepo" />
  </a>
</p>

---

### Let's Connect

<p align="center">
  <a href="https://twitter.com/dunamismax" target="_blank"><img src="https://img.shields.io/badge/Twitter-%231DA1F2.svg?&style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter"></a>
  <a href="https://bsky.app/profile/dunamismax.bsky.social" target="_blank"><img src="https://img.shields.io/badge/Bluesky-blue?style=for-the-badge&logo=bluesky&logoColor=white" alt="Bluesky"></a>
  <a href="https.reddit.com/user/dunamismax" target="_blank"><img src="https://img.shields.io/badge/Reddit-%23FF4500.svg?&style=for-the-badge&logo=reddit&logoColor=white" alt="Reddit"></a>
  <a href="https://discord.com/users/dunamismax" target="_blank"><img src="https://img.shields.io/badge/Discord-dunamismax-7289DA.svg?style=for-the-badge&logo=discord&logoColor=white" alt="Discord"></a>
  <a href="https.signal.me/#p/+dunamismax.66" target="_blank"><img src="https://img.shields.io/badge/Signal-dunamismax.66-3A76F0.svg?style=for-the-badge&logo=signal&logoColor=white" alt="Signal"></a>
</p>
