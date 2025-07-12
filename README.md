<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Go_Logo_Blue.svg/1920px-Go_Logo_Blue.svg.png" alt="The Go programming language logo." width="150"/>
</p>

<p align="center">
  <a href="https://github.com/dunamismax/go-modern-scaffold">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=24&pause=1000&color=00ADD8&center=true&vCenter=true&width=800&lines=IT+Director+%7C+Go+Developer;Creator+of+The+Go-Modern+Stack;Go+%2B+Fiber+%2B+HTMX+%2B+Tailwind;Interactive%2C+Performant%2C+and+Beautiful;Clone%2C+Configure%2C+and+Deploy!" alt="Typing SVG" />
  </a>
</p>

With over a decade of IT experience, I specialize in building fast, maintainable, and powerful applications with Go. I have authored two distinct, production-ready Go stacks to suit different development philosophies:

1. **[The Go-Modern Stack](https://github.com/dunamismax/go-modern-scaffold)**: A feature-rich, batteries-included architecture for building highly interactive and visually appealing web applications with maximum velocity.
2. **[The Pure Go Standard Library Stack](https://github.com/dunamismax/go-stdlib-scaffold)**: A minimalist, dependency-free blueprint for developers who value ultimate simplicity and long-term stability.

Both stacks are available as ready-to-clone templates, each with a complete and self-contained development ecosystem orchestrated by a powerful `magefile.go`.

---

### My Featured Scaffolds

These repositories are the official reference implementations for my two Go stacks. They are living projects that serve as powerful, real-world templates for building robust web applications.

<p align="center">
  <a href="https://github.com/dunamismax/go-modern-scaffold">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=dunamismax&repo=go-modern-scaffold&theme=dracula&show_owner=true" alt="go-modern-scaffold Repository" />
  </a>
  <a href="https://github.com/dunamismax/go-stdlib-scaffold">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=dunamismax&repo=go-stdlib-scaffold&theme=dracula&show_owner=true" alt="go-stdlib-scaffold Repository" />
  </a>
</p>

---

<p align="center">
  <img src="https://user-images.githubusercontent.com/3185864/32058716-5ee9b512-ba38-11e7-978a-287eb2a62743.png" alt="Gopher Mage." width="150"/>
</p>

### The Ultimate Workflow: The `Magefile`

One of the standout features of both scaffold templates is the **`magefile.go`**. This isn't just a build script; it's a complete, Go-native task runner that orchestrates the entire development lifecycle. It provides a seamless, cross-platform experience without ever leaving the Go ecosystem.

**Why is it so great?**

- **Simplicity:** Manage complex workflows with simple commands like `mage dev` or `mage check:all`.
- **Consistency:** Ensures every developer on a project uses the exact same commands for building, testing, and quality checks.
- **Extensibility:** It's written in pure Go, making it easy to customize and extend for any project-specific needs.

With a single command, you can run a comprehensive suite of tests, build production-ready binaries, and manage database migrations. It's designed to make you productive from the very first minute.

---

### My Go Toolkit

My toolkit is a reflection of the two stacks I've created: one focused on a rich, modern toolset and the other on pure, dependency-free simplicity. Both are centered around a superior developer experience with Go at the core.

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=go,fiber,tailwind,docker,postgres,redis,sqlite,linux,ubuntu" />
  </a>
</p>

<details open>
<summary><h3>The Go-Modern Stack (Click to Expand)</h3></summary>

---

This stack is architected for developers aiming to build feature-rich, visually appealing, and highly interactive web and command-line applications with Go. It strategically combines powerful, community-vetted libraries with core Go idioms for a productive and ergonomic development experience. The result is a stack that prioritizes speed, type safety, and modern design without compromising on the core strengths of Go.

---

#### **Frontend: Rich, Interactive & Beautifully Styled**

- [**Templ**](https://templ.guide/): Type-Safe, Component-Based HTML Templating.
- [**Tailwind CSS**](https://tailwindcss.com/docs/installation): Utility-First CSS Framework.
- [**DaisyUI**](https://daisyui.com/): Component Library for Tailwind CSS.
- [**HTMX**](https://htmx.org/docs/): HTML-driven Interactivity.
- [**Hyperscript**](https://hyperscript.org/): Expressive, Event-Driven Scripting.
- [**Animate.css**](https://animate.style/): Drop-in CSS Animation Library.

---

#### **Backend: Ergonomic, Performant & Well-Structured**

- [**Fiber**](https://docs.gofiber.io/): High-Performance Web Framework.
- [**slog**](https://pkg.go.dev/log/slog): Structured, Level-Based Logging.
- [**Viper**](https://github.com/spf13/viper): Complete Configuration Management.
- [**Validator**](https://pkg.go.dev/github.com/go-playground/validator/v10): Struct-Tag Based Data Validation.

---

#### **TUI (Terminal User Interface): Beautiful & Interactive Command-Line Apps**

- [**Bubble Tea**](https://github.com/charmbracelet/bubbletea): Stateful TUI Framework.
- [**Bubbles**](https://github.com/charmbracelet/bubbles): Reusable TUI Components.
- [**Lipgloss**](https://github.com/charmbracelet/lipgloss): Declarative Terminal Styling.

---

#### **Database & Caching: Type-Safe, Performant & Scalable**

- [**sqlc**](https://docs.sqlc.dev/): Type-Safe SQL Code Generation.
- [**Atlas**](https://atlasgo.io/): Database Schema Migrations.
- [**Ristretto**](https://github.com/dgraph-io/ristretto): High-Performance In-Process Cache.
- [**go-redis**](https://redis.io/docs/clients/go/): Redis Client for Distributed Caching.

---

#### **Development Workflow: Automated, Rapid & High-Quality**

- [**Mage**](https://magefile.org/): Task Runner / Build System.
- [**Air**](https://github.com/cosmtrek/air): Live Reloading for Development.
- [**GolangCI-Lint**](https://golangci-lint.run/): Code Quality Linter Aggregator.
- [**Prettier Tailwind CSS Plugin**](https://github.com/tailwindlabs/prettier-plugin-tailwindcss): Automatic Class Sorting.

</details>

<details>
<summary><h3>The Pure Go Standard Library Stack (Click to Expand)</h3></summary>

---

This stack represents a minimalist, robust architecture for building secure and performant web applications. It is composed entirely of a Go backend that leverages the standard library, removing all external dependencies. The stack prioritizes ultimate simplicity, zero-dependency deployment, and long-term stability by relying exclusively on Go's continuously evolving native capabilities. The frontend is reduced to plain HTML and CSS, with no JavaScript.

---

#### **Frontend**

- [**Go `html/template`**](https://pkg.go.dev/html/template): Secure HTML Templating.
- [**Plain CSS**](https://developer.mozilla.org/en-US/docs/Web/CSS): Styling.

---

#### **Backend**

- [**Go (1.22+)**](https://go.dev/doc/): Backend Language.
- [**`net/http`**](https://pkg.go.dev/net/http): Web Server & Advanced Routing.
- [**Custom Validation Functions**](https://www.alexedwards.net/blog/validation-snippets-for-go): Data Validation.
- [**`os`**](https://pkg.go.dev/os): Secure Filesystem Access & Environment Loading.

---

#### **Database & Caching**

- [**SQLite**](https://www.sqlite.org/docs.html): Embedded Relational Database.
- [**`database/sql`**](https://pkg.go.dev/database/sql): SQL Database Interface.
- [**SQL/Go Migration Scripts**](https://amacneil.github.io/dbmate/2022/01/21/go-database-migrations-without-orm.html): Database Schema Migrations.
- [**`sync` & `maps`**](https://pkg.go.dev/sync): High-Performance In-Process Caching.

---

#### **CLI, Development & Deployment**

- [**`flag`**](https://pkg.go.dev/flag): Command-Line Interface.
- [**Mage / Magefile**](https://magefile.org/): Task Runner / Build System.
- [**Simple Shell Scripts**](https://dev.to/ignatk/go-live-reloading-with-a-shell-script-2305): Live Reloading.

</details>

---

### Support My Work

If you find my work on these Go stacks valuable, please consider supporting me. It helps me dedicate more time to creating and maintaining high-quality open-source projects.

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
