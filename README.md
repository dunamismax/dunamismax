# Hi there, I'm dunamismax

<p align="center">
  <a href="https://github.com/dunamismax">
    <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=24&pause=1000&color=4B8BBE&center=true&vCenter=true&width=800&lines=IT+Director.+%7C+Python+Developer.;Building+with+The+Python+Hypermedia+Stack.;FastAPI+%2B+HTMX+%2B+Tailwind+CSS." alt="Typing SVG" />
  </a>
</p>

I'm an IT Director with over 15 years of experience in system administration, VoIP, and web hosting. I am now focused on mastering **Python** to build robust, modern, and high-performance server-rendered web applications. My development philosophy centers on **The Python Hypermedia Stack**: a curated set of tools designed for maximum productivity and minimal frontend complexity.

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

### My Python Toolkit

My toolkit is built around performance, type-safety, and a superior developer experience.

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=python,fastapi,tailwind,htmx,docker,git,github,vscode,linux,ubuntu,bash" />
  </a>
</p>

<details>
<summary><h3>The Python Hypermedia Stack (Click to Expand)</h3></summary>

This stack is designed for building self-contained, high-performance, and interactive web applications. The architecture is centered around a powerful Python backend that renders HTML, enhanced with a minimal set of best-in-class libraries to create a rich user experience without the need for a heavy client-side framework.

---

### **1. Backend**

The core of the application, responsible for handling logic, routing, and rendering the user interface.

- **FastAPI**
  - **Why:** A modern, high-performance Python web framework ideal for building APIs and, in this case, serving server-rendered HTML. It uses standard Python type hints for data validation, which leads to robust, editor-friendly code. It will handle the routes and render the Jinja2 templates.
  - **Latest Version:** 0.111.0
  - **Official Documentation:** <https://fastapi.tiangolo.com/>
- **Uvicorn**
  - **Why:** A lightning-fast ASGI (Asynchronous Server Gateway Interface) server that is required to run FastAPI's asynchronous capabilities. It acts as the direct process manager for the Python application on your server.
  - **Latest Version:** 0.30.1
  - **Official Documentation:** <https://www.uvicorn.org/>

### **2. Database & Data Modeling**

This combination provides a powerful and Python-native way to define, validate, and interact with your database.

- **Pydantic**
  - **Why:** The backbone for data validation in FastAPI. It uses Python type hints to validate, serialize, and deserialize data, ensuring that all data flowing through your application is well-structured and correct. It's a core dependency of FastAPI.
  - **Latest Version:** 2.8.2
  - **Official Documentation:** <https://docs.pydantic.dev/>
- **SQLAlchemy**
  - **Why:** The premier SQL toolkit and Object Relational Mapper (ORM) for Python. It provides a full suite of powerful tools for interacting with your database, offering both a high-level ORM and a low-level SQL expression language for maximum flexibility and performance.
  - **Latest Version:** 2.0.31
  - **Official Documentation:** <https://www.sqlalchemy.org/>
- **SQLModel**
  - **Why:** Created by the author of FastAPI, SQLModel simplifies interaction between the database and the API. It is built on top of Pydantic and SQLAlchemy, allowing you to define your data models, database tables, and API responses from a single, clear Python class. This reduces code duplication significantly.
  - **Latest Version:** 0.1.1
  - **Official Documentation:** <https://sqlmodel.tiangolo.com/>

### **3. Frontend (The Hypermedia Stack)**

This stack creates a rich, interactive user experience by rendering HTML on the server, avoiding the need for a complex client-side JavaScript framework.

- **Jinja2**
  - **Why:** A fast, expressive, and widely-used templating engine for Python. FastAPI will use Jinja2 to render your HTML templates, injecting dynamic data from the backend before sending the final HTML page to the user's browser.
  - **Latest Version:** 3.1.4
  - **Official Documentation:** <https://jinja.palletsprojects.com/>
- **HTMX**
  - **Why:** This is the key to modern interactivity in this stack. HTMX allows you to access modern browser features like AJAX directly from HTML attributes. Instead of writing JavaScript to fetch data and update the UI, you can add simple attributes to your HTML elements that tell HTMX to fetch a new piece of HTML from the server and swap it into the page.
  - **Latest Version:** 2.0.1
  - **Official Documentation:** <https://htmx.org/>
- **Tailwind CSS**
  - **Why:** A utility-first CSS framework that allows for rapid UI development directly within your HTML. Instead of writing custom CSS files, you use pre-defined utility classes. This is highly efficient for prototyping and building custom designs without leaving your Jinja2 templates.
  - **Latest Version:** 3.4.4
  - **Official Documentation:** <https://tailwindcss.com/docs/>
- **DaisyUI**
  - **Why:** A plugin for Tailwind CSS that provides pre-styled components (like buttons, cards, menus, etc.) as Tailwind utility classes. This dramatically speeds up development by giving you beautifully designed components out-of-the-box, while still allowing for full customization through standard Tailwind utilities.
  - **Latest Version:** 4.12.10
  - **Official Documentation:** <https://daisyui.com/>
- **TypeScript (Vanilla)**
  - **Why:** As requested, for minimal, "sprinkled-in" use. While HTMX handles the vast majority of interactivity, you might occasionally need a small, self-contained script for a purely client-side interaction (e.g., toggling a class on a complex element without a server trip). Using vanilla TypeScript provides type-safety for these small, targeted use cases.
  - **Latest Version:** 5.5.3
  - **Official Documentation:** <https://www.typescriptlang.org/docs/>

### **4. CLI & Management**

Tools for creating command-line interfaces to manage the application, run scripts, and automate tasks.

- **Typer**
  - **Why:** The sister library to FastAPI, also built by Sebastián Ramírez. Typer makes it incredibly easy to build powerful and elegant CLI applications using the same Python type hints you use in the rest of the stack. It's ideal for creating management commands (e.g., creating a superuser, seeding the database, running maintenance tasks) with automatic help text and argument validation.
  - **Latest Version:** 0.12.3
  - **Official Documentation:** <https://typer.tiangolo.com/>

### **5. Deployment & Hosting**

Your specified self-hosted deployment on a Linux virtual machine.

- **Ubuntu Server**
  - **Why:** A stable, popular, and well-documented Linux distribution, making it an excellent choice for a web server. The Long-Term Support (LTS) version ensures security updates and stability for years.
  - **Latest Version:** 24.04 LTS ("Noble Numbat")
  - **Official Documentation:** <https://ubuntu.com/server/docs>
- **Caddy**
  - **Why:** An incredibly powerful and easy-to-use web server that excels as a reverse proxy. Its killer feature is automatic HTTPS, meaning it will provision and renew TLS certificates for your domains automatically. Its configuration file (the Caddyfile) is famously simple compared to alternatives. It will sit in front of your Uvicorn process, handling incoming traffic and routing it to your FastAPI application.
  - **Latest Version:** 2.8.4
  - **Official Documentation:** <https://caddyserver.com/docs/>

</details>

---

### My Python Monorepo

I am documenting my progress and projects in my **Python-Hypermedia** monorepo. It is the central hub for all my applications and experiments, putting the Python Hypermedia Stack into practice.

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png" alt="The Python programming language logo." width="100"/>
</p>

<p align="center">
  <a href="https://github.com/dunamismax/Python-Hypermedia">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=dunamismax&repo=Python-Hypermedia&theme=dracula" alt="Python-Hypermedia Monorepo" />
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
