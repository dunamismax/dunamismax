# Hi there, I'm dunamismax 👋

<p align="center">
  <a href="https://github.com/dunamismax">
    <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=24&pause=1000&color=4B8BBE&center=true&vCenter=true&width=800&lines=IT+Director+%7C+Python+Developer;Mastering+Modern+Web+Development.;Building+with+The+Python+Hypermedia+Stack.;FastAPI+%2B+HTMX+%2B+uv+%2B+PostgreSQL;Minimal+JavaScript.+Maximum+Performance.;Check+out+my+Python-Hypermedia+repo+below!" alt="Typing SVG" />
  </a>
</p>

I'm an IT Director with over 12 years of experience, now passionately focused on mastering **Python** to build robust, modern, and high-performance server-rendered web applications.

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
    <img src="https://skillicons.dev/icons?i=python,fastapi,htmx,postgresql,linux,ubuntu" />
  </a>
</p>

<details>
<summary><h3>The Python Hypermedia Stack (Click to Expand)</h3></summary>

This Python Hypermedia Stack is a masterclass in modern web development, thoughtfully curating a suite of best-in-class tools to create a cohesive and powerful development experience. Its commitment to a fully asynchronous backend, paired with a hypermedia-driven frontend, represents a forward-thinking approach that champions simplicity, performance, and maintainability. This stack is a testament to the idea that you can build highly interactive, secure, and scalable web applications without the heavy complexity of traditional frontend frameworks, making it an elegant and productive choice for any development team.

---

### **1. Development & Tooling**

A streamlined toolchain for a productive and consistent development environment, ensuring rapid iteration and high code quality.

- [**uv**](https://astral.sh/uv)
  - **Why:** The next-generation, high-performance Python packaging tool. `uv` is central to all project environment and dependency management, providing an incredibly fast and reliable solution for reproducible environments.
- [**Ruff**](https://docs.astral.sh/ruff/)
  - **Why:** An extremely fast, all-in-one Python linter and code formatter. Ruff ensures consistent code quality and style across the project with a single, cohesive, and blazing-fast utility, integrating seamlessly into the development workflow.

### **2. Backend**

The application's core, built on a fully asynchronous foundation for maximum speed, concurrency, and efficient handling of web requests.

- [**FastAPI**](https://fastapi.tiangolo.com/)
  - **Why:** A modern, high-performance Python web framework. It leverages standard Python type hints for robust APIs and efficient server-side HTML template rendering, forming the backbone of the application.
- [**Uvicorn**](https://www.uvicorn.org/)
  - **Why:** A lightning-fast ASGI server that runs the FastAPI application. Uvicorn serves as the high-performance process manager for both development and production, ensuring rapid response times.
- [**HTTPX**](https://www.python-httpx.org/)
  - **Why:** A fully featured, modern HTTP client for Python. It provides both synchronous and asynchronous APIs, making it the ideal choice for a FastAPI application to interact with external services without blocking the event loop, maintaining responsiveness.

### **3. Database & Migrations**

A unified and fully asynchronous approach to data modeling, interaction, and schema evolution, ensuring data integrity and performance.

- [**PostgreSQL**](https://www.postgresql.org/docs/)
  - **Why:** A powerful, open-source object-relational database system renowned for its reliability, extensive features, and high performance, serving as the robust data store.
- [**SQLModel**](https://sqlmodel.tiangolo.com/)
  - **Why:** The primary tool for database interaction. SQLModel cleverly combines Pydantic and SQLAlchemy, allowing you to define data models, database tables, and API models in a single, elegant Python class, simplifying data management.
- [**Alembic**](https://alembic.sqlalchemy.org/en/latest/)
  - **Why:** A lightweight database migration tool designed for SQLAlchemy (which powers SQLModel) to manage the lifecycle of your database schema, enabling seamless evolution of the database structure.
- [**asyncpg**](https://magicstack.github.io/asyncpg/current/)
  - **Why:** A high-performance, asyncio-native database driver for PostgreSQL. `asyncpg` is the essential link between the asynchronous framework and the database, ensuring all database communication is non-blocking and highly efficient.

### **4. Asynchronous Task Processing**

A native, lightweight system for handling background tasks that should not block the response to the client, ensuring a smooth user experience.

- [**FastAPI BackgroundTasks**](https://fastapi.tiangolo.com/tutorial/background-tasks/)
  - **Why:** For short-lived, in-process background tasks, FastAPI's native `BackgroundTasks` feature is the perfect fit. It allows you to run operations like sending notifications or processing data after returning a response, simplifying the architecture by avoiding the need for external dependencies.

### **5. Frontend**

A pure hypermedia-driven frontend that delivers a rich user experience without requiring a complex JavaScript framework or a build step, focusing on server-rendered HTML.

- [**Jinja2**](https://jinja.palletsprojects.com/)
  - **Why:** A fast and expressive templating engine used by FastAPI to render dynamic HTML, injecting backend data directly into the user interface, providing a flexible and powerful templating solution.
- [**HTMX**](https://htmx.org/)
  - **Why:** The core of the interactive experience. HTMX allows you to trigger AJAX requests directly from HTML attributes, enabling smooth UI updates by swapping server-rendered HTML fragments without writing complex JavaScript, embracing the hypermedia approach.
- [**Pico.css**](https://picocss.com/)
  - **Why:** A minimalist CSS framework that makes semantic HTML look beautiful by default. By linking to a single CSS file, you get elegant styling for raw HTML elements, automatic dark mode, and responsive design, all without dependencies or a complex setup, aligning with the minimal frontend philosophy.

### **6. Testing**

A powerful and standard framework for ensuring code quality and correctness, providing confidence in the application's reliability.

- [**Pytest**](https://docs.pytest.org/en/stable/)
  - **Why:** The de facto standard testing framework for Python. Pytest makes it easy to write small, readable tests and scales to support complex functional testing, with excellent support for asynchronous code via plugins like `pytest-asyncio`.

### **7. CLI, Security & Configuration**

Modern tools for building command-line interfaces, securing the application, and managing configuration, enhancing developer productivity and application robustness.

- [**Typer**](https://typer.tiangolo.com/)
  - **Why:** A library for building powerful and user-friendly CLI applications. It uses the same Python type-hint philosophy as FastAPI, making it intuitive to create administrative commands and automate tasks.

### **8. Deployment**

A self-hosted, secure, and stable production environment, optimized for the Python Hypermedia Stack.

- [**Ubuntu Server (LTS)**](https://ubuntu.com/server)
  - **Why:** A popular, stable, and well-documented Linux distribution ideal for web servers, with long-term support for security and maintenance updates, providing a reliable foundation for deployment.
- [**Caddy**](https://caddyserver.com/docs/)
  - **Why:** A modern, powerful web server and reverse proxy with a focus on simplicity. Caddy manages incoming traffic, serves static files, and acts as a reverse proxy for Uvicorn. Its standout feature is fully automatic HTTPS, simplifying secure deployments.

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
