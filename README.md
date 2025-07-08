# Hi there, I'm dunamismax

<p align="center">
  <a href="https://github.com/dunamismax">
    <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=24&pause=1000&color=00ADD8&center=true&vCenter=true&width=800&lines=IT+Director.+%7C+Golang+Developer.;Building+with+The+Pragmatic+Go+Stack.;Standard+Library+First.+Minimal+Dependencies." alt="Typing SVG" />
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
<summary><h3>The Pragmatic Go Stack (Click to Expand)</h3></summary>

This stack is designed for building self-contained, high-performance, and concurrent web applications. The architecture is centered around the Go standard library, supplemented by a minimal set of highly-regarded libraries to enhance productivity and security. This approach yields a robust, minimal-dependency application that is simple to deploy and maintain.

---

#### **Core Application & CLI**

- **Language:** [**Go**](https://go.dev/doc/) (v1.22+)
  - A statically typed, compiled language that serves as the application's foundation, known for its performance, native concurrency, and single-binary deployments.
- **Web Router:** [**`net/http`**](https://pkg.go.dev/net/http/)
  - The standard library's production-grade HTTP server and multiplexer (`http.ServeMux`), used to route incoming requests to the appropriate handler functions.
- **CLI Framework:** [**`flag`**](https://pkg.go.dev/flag/)
  - The standard library package for parsing command-line flags, used to configure the application's behavior at startup.
- **Database ORM:** [**GORM**](https://gorm.io/docs/)
  - A full-featured Object-Relational Mapper for Golang that provides a developer-friendly API for database interactions, simplifying common CRUD operations, queries, and schema management.
- **Database Access:** [**`database/sql`**](https://pkg.go.dev/database/sql/)
  - The standard library's generic SQL interface. It provides the underlying foundation upon which GORM and the database driver operate, ensuring stability and standardization.
- **Database Driver (PostgreSQL):** [**`lib/pq`**](https://pkg.go.dev/github.com/lib/pq)
  - A widely-used and stable PostgreSQL driver for Go. It implements the standard `database/sql` interface, enabling the application to communicate with a PostgreSQL database.
- **Database Migrations:** [**`golang-migrate/migrate`**](https://pkg.go.dev/github.com/golang-migrate/migrate/v4)
  - A dedicated tool that manages database schema changes using versioned SQL files, runnable as a CLI or a library for robust version control.

#### **Developer Experience & Tooling**

- **Package & Environment Management:** [**Go Modules & Toolchain**](https://go.dev/doc/tool/)
  - The native Go toolchain manages dependencies, builds, testing, and other development tasks, providing a unified and consistent experience.
- **Linter & Formatter:** [**`go fmt`**](https://pkg.go.dev/cmd/gofmt/) & [**`go vet`**](https://pkg.go.dev/cmd/vet/)
  - `go fmt` automatically formats code to the canonical Go style, and `go vet` is a static analyzer that reports suspicious code constructs to help find bugs.
- **Configuration:** [**Viper**](https://pkg.go.dev/github.com/spf13/viper)
  - A complete configuration solution handling various formats (JSON, TOML, YAML), environment variables, and remote config systems.
- **Live Reloading:** [**Air**](https://github.com/air-verse/air)
  - A live-reloading command-line utility for Go applications. Air monitors file changes in the project directory and automatically recompiles and restarts the application, streamlining the development feedback loop.

#### **Frontend & User Experience**

- **Client-Side Interactivity:** [**htmx**](https://htmx.org/docs/) (v2.0.0)
  - A compact JavaScript library that enables modern user experiences like AJAX requests and partial page updates directly within HTML attributes, eliminating the need for custom client-side JavaScript. The library is served as a static asset.
- **Templating:** [**`html/template`**](https://pkg.go.dev/html/template/)
  - The standard library's server-side HTML rendering engine. It provides fast, secure templating with context-aware escaping to automatically prevent Cross-Site Scripting (XSS) vulnerabilities.
- **Go/htmx Integration:** **Standard Handlers**
  - Integration is achieved using standard `http.HandlerFunc` implementations. These handlers process requests and write back either full HTML documents or partial template fragments to the `http.ResponseWriter`, seamlessly responding to htmx-driven interactions.
- **Forms & Validation:** **Manual Struct Population & Methods**
  - Form data is parsed from incoming requests using `r.ParseForm()`, and the values are used to manually populate data structs. Validation logic is implemented as explicit methods on these structs for clear and precise control.
- **Client-Side Validation:** [**HTML5 Validation**](https://developer.mozilla.org/en-US/docs/Learn/Forms/Form_validation#using_built-in_form_validation)
  - Built-in browser features provide instant client-side validation for a responsive user experience, acting as the first line of defense for data integrity.

#### **Authentication**

- **Core Authentication:** [**`golang.org/x/crypto/bcrypt`**](https://pkg.go.dev/golang.org/x/crypto/bcrypt) & [**`crypto`**](https://pkg.go.dev/crypto/) Packages
  - Password security is handled using the industry-standard `bcrypt` hashing algorithm, provided by the official Go crypto repository. For session management, JSON Web Tokens (JWTs) are constructed and verified using the standard library's `crypto/hmac` and `encoding/base64` packages.

#### **Deployment & Production**

- **Web Server / Reverse Proxy:** [**Caddy**](https://caddyserver.com/docs/) (v2)
  - A production-grade, open-source web server with automatic HTTPS. It serves as a reverse proxy, securely routing traffic to the compiled Go application binary.
- **Asset Management:** [**`embed`**](https://pkg.go.dev/embed/)
  - The standard library's `embed` package bundles static assets—including CSS, images, and the `htmx.js` library—directly into the Go binary at compile time. This creates a single, self-contained executable that is incredibly easy to deploy.

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
