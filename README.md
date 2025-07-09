# Hi there, I'm dunamismax 👋

<p align="center">
  <a href="https://github.com/dunamismax">
    <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=24&pause=1000&color=4B8BBE&center=true&vCenter=true&width=800&lines=IT+Director+%7C+Python+Developer;Mastering+Modern+Web+Development.;Building+with+The+Python+Hypermedia+Stack.;FastAPI+%2B+HTMX+%2B+uv+%2B+Tailwind+CSS;Minimal+JavaScript.+Maximum+Performance.;Check+out+my+Python-Hypermedia+repo+below!" alt="Typing SVG" />
  </a>
</p>

I'm an IT Director with over 12 years of experience who is now passionately focused on mastering **Python** to build robust, modern, and high-performance server-rendered web applications.

My development philosophy centers on **The Python Hypermedia Stack**: a curated set of best-in-class tools designed for maximum productivity and minimal frontend complexity. I believe in lean, powerful backends that deliver a rich user experience directly from the server. All my development is done on **macOS**, using **uv** for a lightning-fast workflow, and deployed to self-hosted **Linux (Ubuntu)** servers.

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

### My Python Toolkit

My toolkit is built around performance, type-safety, and a superior developer experience with **uv** at the core.

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=python,fastapi,htmx,tailwind,docker,git,github,vscode,linux,ubuntu,bash" />
  </a>
</p>

<details>
<summary><h3>The Python Hypermedia Stack (Click to Expand)</h3></summary>

This stack is designed for building fast, modern web applications with server-rendered HTML, enhanced with dynamic interactivity. It prioritizes developer experience, performance, and maintainability by leveraging a curated set of modern tools.

### **1. Development & Tooling**

A streamlined toolchain for a productive and consistent development environment.

- [**uv**](https://astral.sh/uv)
  - **Why:** A next-generation, high-performance Python packaging tool. `uv` handles project dependency management and virtual environments with exceptional speed, replacing traditional tools like `pip` and `venv` for a faster, more efficient workflow.
- [**Ruff**](https://docs.astral.sh/ruff/)
  - **Why:** An extremely fast, all-in-one Python linter and code formatter. Ruff replaces multiple tools (like Black, isort, and Flake8) with a single, cohesive, and blazing-fast utility, ensuring consistent code quality and style across the project.

### **2. Backend**

The application's core, built for speed, resilience, and connectivity.

- [**FastAPI**](https://fastapi.tiangolo.com/)
  - **Why:** A modern, high-performance Python web framework. It uses standard Python type hints to build robust APIs and render server-side HTML templates, providing automatic data validation and documentation.
- [**Gunicorn**](https://gunicorn.org/)
  - **Why:** A battle-tested WSGI HTTP server used as a process manager for Uvicorn in production. Gunicorn manages multiple Uvicorn worker processes, enabling you to leverage multi-core CPUs, increase capacity, and improve fault tolerance.
- [**Uvicorn**](https://www.uvicorn.org/)
  - **Why:** A lightning-fast ASGI server that runs the FastAPI application. In production, it is managed by Gunicorn to run multiple worker processes, enabling high-performance asynchronous capabilities.
- [**HTTPX**](https://www.python-httpx.org/)
  - **Why:** A fully featured, modern HTTP client for Python. It provides both sync and async APIs, making it the ideal choice for a FastAPI application to interact with external services without blocking the event loop.

### **3. Database**

A unified and Pythonic approach to data modeling, interaction, and evolution.

- [**SQLModel**](https://sqlmodel.tiangolo.com/)
  - **Why:** The primary tool for database interaction, built by the creator of FastAPI. SQLModel cleverly combines Pydantic and SQLAlchemy, allowing you to define data, database tables, and API models in a single Python class. This significantly reduces code duplication and simplifies data management.
- [**Alembic**](https://alembic.sqlalchemy.org/en/latest/)
  - **Why:** A powerful database migration tool from the creator of SQLAlchemy. Alembic provides a reliable and systematic way to manage and version changes to your database schema as your application's models evolve.
- [**Pydantic**](https://docs.pydantic.dev/latest/)
  - **Why:** One of the foundational libraries that power SQLModel. Pydantic provides robust data validation and settings management using Python type hints.
- [**SQLAlchemy**](https://www.sqlalchemy.org/)
  - **Why:** One of the foundational libraries that power SQLModel. SQLAlchemy offers a powerful and flexible SQL toolkit and Object Relational Mapper (ORM) for comprehensive database control.

### **4. Frontend**

A hypermedia-driven frontend that delivers a rich user experience without requiring a heavy client-side JavaScript framework.

- [**Jinja2**](https://jinja.palletsprojects.com/)
  - **Why:** A fast and expressive templating engine used by FastAPI to render dynamic HTML, injecting backend data directly into the user interface.
- [**HTMX**](https://htmx.org/)
  - **Why:** The core of the interactive experience. HTMX allows you to trigger AJAX requests directly from HTML attributes, enabling smooth UI updates by swapping server-rendered HTML fragments without writing complex JavaScript.
- [**Tailwind CSS**](https://tailwindcss.com/docs/)
  - **Why:** A utility-first CSS framework for rapidly building custom user interfaces directly within your HTML, promoting speed and consistency in design.
- [**DaisyUI**](https://daisyui.com/)
  - **Why:** A plugin for Tailwind CSS that provides a library of pre-styled components (like buttons, cards, and menus). It accelerates development by offering ready-to-use UI elements that are fully customizable with Tailwind utilities.
- [**TypeScript**](https://www.typescriptlang.org/docs/)
  - **Why:** Used for minimal, targeted client-side interactions where HTMX may not be suitable. Vanilla TypeScript offers type safety for small, self-contained scripts without adding framework overhead.

### **5. CLI & Task Management**

Modern tools for building command-line interfaces and automating development tasks.

- [**Typer**](https://typer.tiangolo.com/)
  - **Why:** A library for building powerful and user-friendly CLI applications, created by the author of FastAPI. It uses the same Python type-hint philosophy, making it intuitive to create commands for database migrations, user management, or other administrative tasks.
- [**Invoke**](https://www.pyinvoke.org/)
  - **Why:** A Python task execution library for defining and running administrative tasks. Invoke is excellent for creating a clean, organized collection of commands for common operations like starting a dev server, running tests, or deploying the application.

### **6. Deployment**

A self-hosted, secure, and stable production environment.

- [**Ubuntu Server (LTS)**](https://ubuntu.com/server/docs)
  - **Why:** A popular, stable, and well-documented Linux distribution ideal for web servers. The Long-Term Support (LTS) version guarantees security and maintenance updates for years.
- [**Caddy**](https://caddyserver.com/docs/)
  - **Why:** A modern, powerful web server and reverse proxy with a focus on simplicity. Caddy's standout feature is fully automatic HTTPS, effortlessly securing your application with zero-touch TLS certificate provisioning and renewal.

</details>

---

### My Current Focus: The Python-Hypermedia Monorepo

I am channeling all my learning and development into my **Python-Hypermedia** monorepo. It is the central hub for all my applications and experiments, putting the Python Hypermedia Stack into practice. This project is a living testament to my development philosophy.

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png" alt="The Python programming language logo." width="100"/>
</p>

<p align="center">
  <a href="https://github.com/dunamismax/Python-Hypermedia">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=dunamismax&repo=Python-Hypermedia&theme=dracula&show_owner=true" alt="Python-Hypermedia Monorepo" />
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
