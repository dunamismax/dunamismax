# Deployment Guide (Ubuntu Server)

This comprehensive guide provides instructions on how to set up, build, and deploy the `dunamismax.com` website. It covers local development setup, Supabase configuration, and self-hosting on an Ubuntu Server using Nginx.

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
5.  [Self-Hosting on Ubuntu Server](#5-self-hosting-on-ubuntu-server)
    *   [Server Preparation](#server-preparation)
    *   [Clone Repository on Server](#clone-repository-on-server)
    *   [Backend Setup on Server](#backend-setup-on-server)
    *   [Frontend Setup on Server](#frontend-setup-on-server)
    *   [Nginx Configuration](#nginx-configuration)
    *   [Running the Application in Production](#running-the-application-in-production)
    *   [Accessing the Self-Hosted Website](#accessing-the-self-hosted-website)

---

## 1. Prerequisites

Before you begin, ensure you have the following installed on your system (for local development) or your Ubuntu Server (for self-hosting):

*   **Node.js (LTS) & npm:** Required for the Next.js frontend.
    *   [Node.js Download](https://nodejs.org/en/download/)
*   **Python 3.9+:** Required for the FastAPI backend.
    *   [Python Download](https://www.python.org/downloads/)
*   **pip (Python Package Installer):** Usually comes with Python.
*   **Git:** For cloning the repository.
    *   [Git Download](https://git-scm.com/downloads)
*   **Supabase Account:** You will need a Supabase account and project for the database and backend services.
    *   [Supabase Website](https://supabase.com/)
*   **Ubuntu Server:** A running Ubuntu Server instance for self-hosting.
*   **Nginx:** A web server that will act as a reverse proxy on your Ubuntu Server.

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

## 5. Self-Hosting on Ubuntu Server

This section details how to deploy and run the `dunamismax.com` website on an Ubuntu Server.

### Server Preparation

First, ensure your Ubuntu server is updated and has the necessary tools installed:

```bash
sudo apt update
sudo apt upgrade -y
sudo apt install -y git python3 python3-pip python3-venv nginx
```

### Clone Repository on Server

Clone the project repository to your Ubuntu server. It's recommended to clone it into a directory like `/var/www/`.

```bash
sudo mkdir -p /var/www/dunamismax.com
sudo chown -R $USER:$USER /var/www/dunamismax.com
git clone https://github.com/dunamismax/dunamismax.git /var/www/dunamismax.com
cd /var/www/dunamismax.com
```

### Backend Setup on Server

Navigate to the `backend` directory, create a virtual environment, install dependencies, and configure environment variables.

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install gunicorn # Install Gunicorn for production
```

**Configure Backend Environment Variables:**

Create a `.env` file in the `backend` directory with your production Supabase credentials. These should be the same as your local `.env` file.

```bash
cp .env.example .env
# Open .env and add your Supabase credentials
```

### Frontend Setup on Server

Navigate to the `frontend` directory, install dependencies, build the Next.js application, and configure environment variables.

```bash
cd ../frontend
npm install
npm run build
```

**Configure Frontend Environment Variables:**

Create a `.env.local` file in the `frontend` directory. For production, `NEXT_PUBLIC_API_BASE_URL` should point to your server's domain or IP address where Nginx will proxy requests to the backend.

```bash
cp .env.local.example .env.local
```

Open `frontend/.env.local` and ensure it contains:

```
NEXT_PUBLIC_API_BASE_URL=http://YOUR_SERVER_IP_OR_DOMAIN:8000 # Or whatever port Nginx will proxy to
NEXT_PUBLIC_SUPABASE_URL="YOUR_SUPABASE_URL"
NEXT_PUBLIC_SUPABASE_ANON_KEY="YOUR_SUPABASE_ANON_KEY"
```

### Nginx Configuration

Nginx will serve the Next.js static assets and proxy API requests to the FastAPI backend.

1.  **Create Nginx Configuration File:**

    ```bash
    sudo nano /etc/nginx/sites-available/dunamismax.com
    ```

    Add the following content to the file. Replace `YOUR_SERVER_IP_OR_DOMAIN` with your actual server IP address or domain name.

    ```nginx
    server {
        listen 80;
        server_name YOUR_SERVER_IP_OR_DOMAIN;

        location / {
            proxy_pass http://localhost:3000; # Next.js frontend
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection 'upgrade';
            proxy_set_header Host $host;
            proxy_cache_bypass $http_upgrade;
        }

        location /api/ {
            proxy_pass http://localhost:8000; # FastAPI backend
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
    ```

2.  **Enable the Nginx Configuration:**

    ```bash
    sudo ln -s /etc/nginx/sites-available/dunamismax.com /etc/nginx/sites-enabled/
    sudo nginx -t
    sudo systemctl restart nginx
    ```

### Running the Application in Production

For production, you should use `gunicorn` to run the FastAPI backend and `pm2` (or `systemd`) to manage both the backend and frontend processes.

1.  **Install PM2:**

    ```bash
    sudo npm install -g pm2
    ```

2.  **Start Backend with Gunicorn and PM2:**

    Navigate to the `backend` directory and start the FastAPI application using Gunicorn and PM2. Ensure your virtual environment is activated.

    ```bash
    cd /var/www/dunamismax.com/backend
    source venv/bin/activate
    pm2 start "gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app" --name "dunamismax-backend"
    ```

    *   `-w 4`: Runs 4 worker processes (adjust based on your server's CPU cores).
    *   `-k uvicorn.workers.UvicornWorker`: Specifies Uvicorn worker class.

3.  **Start Frontend with PM2:**

    Navigate to the `frontend` directory and start the Next.js application with PM2.

    ```bash
    cd /var/www/dunamismax.com/frontend
    pm2 start "npm run start" --name "dunamismax-frontend"
    ```

4.  **Save PM2 Process List (for persistence across reboots):**

    ```bash
    pm2 save
    pm2 startup
    ```

### Accessing the Self-Hosted Website

Open your web browser and navigate to your server's IP address or domain name (e.g., `http://YOUR_SERVER_IP_OR_DOMAIN`). You should see the `dunamismax.com` website.