# Hi there, I'm dunamismax

<p align="center">
  <a href="https://github.com/dunamismax">
    <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=24&pause=1000&color=00ADD8&center=true&vCenter=true&width=800&lines=IT+Director+%7C+Golang+Developer;Building+with+The+Pragmatic+Go+Stack;Standard+Library+First.+Minimal+Dependencies." alt="Typing SVG" />
  </a>
</p>

I'm an IT Director with over 15 years of experience in system administration, VoIP, and web hosting. I am now focused on mastering **Go** to build robust, elegant, and high-performance web applications, APIs, and CLI tools. My development philosophy centers on a **Pragmatic Go Stack**: leveraging the power of the standard library first, supplemented by a minimal set of high-quality tools.

All my development is done on **macOS**, with a focus on deploying to self-hosted **Linux (Ubuntu)** servers.

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

My toolkit is built around simplicity, performance, and a great developer experience.

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=go,postgres,docker,htmx,git,github,vscode,linux,ubuntu,bash" />
  </a>
</p>

<details>
<summary><h3>My Pragmatic Go Stack (Click to Expand)</h3></summary>

This stack is designed for building modern, high-performance, and self-contained web applications. It prioritizes simplicity and maintainability by leaning heavily on Go's powerful standard library and a minimal set of well-vetted, essential third-party libraries.

#### **Core Application & CLI**

- **Language:** [**Go**](https://go.dev/doc/) (v1.22+)
  - The application's foundation. A statically typed, compiled language renowned for performance, native concurrency, and single-binary deployments.
- **Web Router:** [**`net/http`**](https://pkg.go.dev/net/http/)
  - Go's powerful standard library handles all web server and routing needs. Using the built-in `http.ServeMux` provides a robust, dependency-free foundation.
- **CLI Framework:** [**`flag`**](https://pkg.go.dev/flag/)
  - The standard library package for parsing command-line flags, perfect for configuring application behavior at startup without external dependencies.
- **Database ORM:** [**GORM**](https://gorm.io/docs/)
  - A developer-friendly ORM that simplifies database interactions like CRUD, queries, and schema management.
- **Database Driver (PostgreSQL):** [**`lib/pq`**](https://pkg.go.dev/github.com/lib/pq)
  - A popular and stable PostgreSQL driver for Go that works seamlessly with the standard `database/sql` interface.
- **Database Migrations:** [**`golang-migrate/migrate`**](https://pkg.go.dev/github.com/golang-migrate/migrate/v4)
  - A dedicated tool for managing database schema changes using versioned SQL files, ensuring robust and repeatable migrations.

#### **Developer Experience & Tooling**

- **Package & Environment Management:** [**Go Modules & Toolchain**](https://go.dev/doc/tool/)
  - The native Go toolchain provides a unified experience for managing dependencies, builds (`go build`), testing, formatting (`go fmt`), and linting (`go vet`).
- **Configuration:** [**Viper**](https://github.com/spf13/viper)
  - A complete configuration solution handling `.env` files, other formats (JSON, YAML), environment variables, and remote config systems.
- **Live Reloading:** [**Air**](https://github.com/air-verse/air)
  - A command-line tool that automatically rebuilds and restarts the application on file changes, creating a fast and efficient development loop.

#### **Frontend & User Experience**

- **Client-Side Interactivity:** [**htmx**](https://htmx.org/docs/)
  - A small JavaScript library enabling modern AJAX and partial page updates directly in HTML, served by Go handlers.
- **Templating:** **`html/template`**
  - Go's standard library for secure, server-side HTML rendering with automatic, context-aware escaping to prevent XSS attacks.
- **Forms & Validation:** **Manual Struct Population & Methods**
  - Form data is manually parsed and validated using methods on Go structs, providing clear, explicit control over data handling.
- **Client-Side Validation:** **HTML5 Validation**
  - Uses built-in browser validation for instant feedback on user input, providing a great first line of defense.

#### **Authentication**

- **Core Authentication:** **`golang.org/x/crypto/bcrypt`** & **Standard `crypto` Packages**
  - Password security is handled with the industry-standard `bcrypt` hashing algorithm. Session management (e.g., JWTs) is built using Go's standard crypto packages.

#### **Deployment & Production**

- **Web Server / Reverse Proxy:** [**Caddy**](https://caddyserver.com/docs/)
  - A modern web server and reverse proxy with automatic HTTPS, perfect for securely routing traffic to the compiled Go application binary.
- **Asset Management:** [**Go `embed` Package**](https://pkg.go.dev/embed)
  - The standard library `embed` package bundles static assets (CSS, JS, images) directly into the Go binary, creating a single, self-contained executable that is trivial to deploy.

</details>

---

### My Go Monorepo

I am documenting my entire journey in my **Go Monorepo**. It is the central hub for all my applications, services, and experiments, putting the Pragmatic Go Stack into practice. Follow my progress there!

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Go_Logo_Blue.svg/1920px-Go_Logo_Blue.svg.png" alt="The Go programming language logo." width="100"/>
</p>

<table align="center">
  <tr>
    <td align="center">
      <a href="https://github.com/dunamismax/go">
        <img src="https://github-readme-stats.vercel.app/api/pin/?username=dunamismax&repo=go&theme=dracula" alt="Go Monorepo" />
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/dunamismax/go-monorepo-template">
        <img src="https://github-readme-stats.vercel.app/api/pin/?username=dunamismax&repo=go-monorepo-template&theme=dracula" alt="Go Monorepo Template" />
      </a>
    </td>
  </tr>
</table>

---

### Let's Connect

<p align="center">
  <a href="https://twitter.com/dunamismax" target="_blank"><img src="https://img.shields.io/badge/Twitter-%231DA1F2.svg?&style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter"></a>
  <a href="https://bsky.app/profile/dunamismax.bsky.social" target="_blank"><img src="https://img.shields.io/badge/Bluesky-blue?style=for-the-badge&logo=bluesky&logoColor=white" alt="Bluesky"></a>
  <a href="https://reddit.com/user/dunamismax" target="_blank"><img src="https://img.shields.io/badge/Reddit-%23FF4500.svg?&style=for-the-badge&logo=reddit&logoColor=white" alt="Reddit"></a>
  <a href="https://discord.com/users/dunamismax" target="_blank"><img src="https://img.shields.io/badge/Discord-dunamismax-7289DA.svg?style=for-the-badge&logo=discord&logoColor=white" alt="Discord"></a>
  <a href="https://signal.me/#p/+dunamismax.66" target="_blank"><img src="https://img.shields.io/badge/Signal-dunamismax.66-3A76F0.svg?style=for-the-badge&logo=signal&logoColor=white" alt="Signal"></a>
</p>
