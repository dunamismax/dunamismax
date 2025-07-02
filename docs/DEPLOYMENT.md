# Deployment Guide (macOS / Linux)

This comprehensive guide provides instructions on how to set up, build, and deploy the `dunamismax.com` website. It covers local development setup, Supabase configuration, and a high-level overview of self-hosting.

## Table of Contents

1.  [Prerequisites](#1-prerequisites)
2.  [Supabase Setup](#2-supabase-setup)
3.  [Local Development Setup](#3-local-development-setup)
    *   [Clone the Repository](#clone-the-repository)
    *   [Frontend Setup (Next.js)](#frontend-setup-nextjs)
    *   [Backend Setup (FastAPI)](#backend-setup-fastapi)
4.  [Running the Application Locally](#4-running-the-application-locally)
    *   [Start the Backend Server](#start-the-backend-server-fastapi)
    *   [Start the Frontend Server](#start-the-frontend-server-nextjs)
    *   [Accessing the Website](#accessing-the-website)
    *   [Stopping the Application](#stopping-the-application)
5.  [Self-Hosting / Deployment Overview](#5-self-hosting--deployment-overview)
    *   [Frontend Deployment](#frontend-deployment)
    *   [Backend Deployment](#backend-deployment)

---

## 1. Prerequisites

Before you begin, ensure you have the following installed on your system:

*   **Node.js (LTS) & npm:** Required for the Next.js frontend.
    *   [Node.js Download](https://nodejs.org/en/download/)
*   **Python 3.9+:** Required for the FastAPI backend.
    *   [Python Download](https://www.python.org/downloads/)
*   **pip (Python Package Installer):** Usually comes with Python.
*   **Git:** For cloning the repository.
    *   [Git Download](https://git-scm.com/downloads)
*   **Supabase Account:** You will need a Supabase account and project for the database and backend services.
    *   [Supabase Website](https://supabase.com/)

## 2. Supabase Setup

Follow these steps to set up your Supabase project and database for the blog functionality:

1.  **Create a New Supabase Project:**
    *   Go to your [Supabase Dashboard](https://app.supabase.com/).
    *   Click on `New project`.
    *   Fill in the required details (Name, Database Password, Region) and click `Create new project`.

2.  **Get Your Supabase Credentials:**
    *   Once your project is created, navigate to `Project Settings` > `API`.
    *   Note down your `Project URL` and `anon public` key. You will need these for your environment variables.

3.  **Create the `blog_posts` Table:**
    *   In your Supabase project dashboard, go to `Table Editor`.
    *   Click `New table`.
    *   **Name:** `blog_posts`
    *   **Schema:** `public` (default)
    *   **Enable Row Level Security (RLS):** Keep this enabled for security best practices. You will need to define policies later if you want to allow public read access or authenticated write access.
    *   **Columns:** Add the following columns:
        *   `id`: `int8`, Primary Key, `Is Identity` (auto-increments)
        *   `title`: `text`
        *   `content`: `text`
        *   `created_at`: `timestamptz`, Default Value: `now()`
    *   Click `Save`.

4.  **Insert Sample Data (Optional but Recommended):**
    *   Go to the `Table Editor` for your `blog_posts` table.
    *   Click `Insert row`.
    *   Add a few sample blog posts with a `title` and `content` to test the application.

## 3. Local Development Setup

### Clone the Repository

First, clone the project repository to your local machine:

```bash
git clone https://github.com/dunamismax/dunamismax.git
cd dunamismax
```

### Frontend Setup (Next.js)

Navigate to the `frontend` directory and install the JavaScript dependencies:

```bash
cd frontend
npm install
```

**Configure Frontend Environment Variables:**

Create a `.env.local` file in the `frontend` directory and add your Supabase credentials and the backend API base URL. Replace the placeholder values with your actual Supabase Project URL and Anon Key.

```bash
cp .env.local.example .env.local # If you don't have .env.local already
```

Open `frontend/.env.local` and ensure it contains:

```
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
NEXT_PUBLIC_SUPABASE_URL="YOUR_SUPABASE_URL"
NEXT_PUBLIC_SUPABASE_ANON_KEY="YOUR_SUPABASE_ANON_KEY"
```

### Backend Setup (FastAPI)

Open a **new terminal**, navigate to the `backend` directory, and install the Python dependencies. It's highly recommended to use a virtual environment to manage your Python packages.

```bash
cd ../backend
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```

**Configure Backend Environment Variables:**

Create a `.env` file in the `backend` directory and add your Supabase credentials. Replace the placeholder values with your actual Supabase Project URL and Anon Key.

```bash
cp .env.example .env # If you don't have .env already
```

Open `backend/.env` and ensure it contains:

```
SUPABASE_URL="YOUR_SUPABASE_URL"
SUPABASE_KEY="YOUR_SUPABASE_ANON_KEY"
```

## 4. Running the Application Locally

To run the full application, you will need to start both the frontend and backend servers concurrently in separate terminal windows.

### Start the Backend Server (FastAPI)

In the terminal where you set up the `backend` (and activated your virtual environment), run:

```bash
uvicorn main:app --reload
```

This will start the FastAPI server, typically on `http://127.0.0.1:8000`. You should see output indicating the server is running.

### Start the Frontend Server (Next.js)

Open a **new terminal**, navigate to the `frontend` directory, and run:

```bash
cd ../frontend
npm run dev
```

This will start the Next.js development server, typically on `http://localhost:3000`. The Next.js application will automatically proxy API requests to the FastAPI backend.

### Accessing the Website

Once both servers are running, open your web browser and navigate to:

`http://localhost:3000`

You should now see the `dunamismax.com` website, with blog posts fetched from your Supabase database.

### Stopping the Application

To stop both servers, go to each terminal where they are running and press `Ctrl + C`.

## 5. Self-Hosting / Deployment Overview

Deploying this full-stack application involves separate steps for the frontend and backend due to their decoupled nature.

### Frontend Deployment

The Next.js frontend is a static site with server-side rendering capabilities. It can be deployed to various platforms optimized for Next.js applications, such as:

*   **Vercel (Recommended for Next.js):** The creators of Next.js, Vercel provides seamless deployment and excellent performance for Next.js applications.
*   **Netlify:** Another popular choice for static sites and Next.js.
*   **Custom Server (e.g., Ubuntu with Caddy/Nginx and PM2):** You can build the Next.js application (`npm run build`) and then serve the output (`.next` folder) using a web server like Caddy or Nginx, managed by PM2 or systemd.

**Key steps for Frontend Deployment:**
1.  **Build:** Run `npm run build` in the `frontend` directory. This generates the optimized production build.
2.  **Environment Variables:** Ensure your production environment variables (`NEXT_PUBLIC_API_BASE_URL`, `NEXT_PUBLIC_SUPABASE_URL`, `NEXT_PUBLIC_SUPABASE_ANON_KEY`) are correctly configured on your hosting platform. `NEXT_PUBLIC_API_BASE_URL` should point to your deployed FastAPI backend URL.
3.  **Serve:** Configure your chosen hosting platform or web server to serve the built Next.js application.

### Backend Deployment

The FastAPI backend is a Python application that can be deployed using various methods, often involving containerization for consistency and scalability.

*   **Docker (Recommended):** Containerize your FastAPI application with Gunicorn and Uvicorn. This provides a portable and isolated deployment unit.
*   **Cloud Platforms (e.g., DigitalOcean Droplet, AWS EC2, Heroku):** Deploy your Docker container or Python application directly to a cloud virtual machine or platform-as-a-service.
*   **Custom Server (e.g., Ubuntu with Gunicorn/Uvicorn and systemd/PM2):** Install Python, create a virtual environment, install dependencies, and run your FastAPI application with Gunicorn (for production-grade process management) behind a reverse proxy like Caddy or Nginx.

**Key steps for Backend Deployment:**
1.  **Containerization (Optional but Recommended):** Create a `Dockerfile` to build a Docker image of your FastAPI application.
2.  **Process Management:** Use a production-ready ASGI server like Gunicorn with Uvicorn workers to run your FastAPI application. Manage this process with `systemd` or `PM2` for reliability.
3.  **Reverse Proxy:** Place a reverse proxy (e.g., Caddy, Nginx) in front of your FastAPI application to handle SSL termination, load balancing, and static file serving.
4.  **Environment Variables:** Configure your production environment variables (`SUPABASE_URL`, `SUPABASE_KEY`) on your server or hosting platform.

This guide provides a solid foundation. For specific deployment scenarios, refer to the documentation of your chosen hosting platform and tools.