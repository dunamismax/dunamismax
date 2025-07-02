# Build and Run Guide (macOS / Linux)

This guide provides instructions on how to set up, build, and run the `dunamismax.com` website locally on macOS and Linux environments.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

*   **Node.js (LTS) & npm:** Required for the Next.js frontend.
    *   [Node.js Download](https://nodejs.org/en/download/)
*   **Python 3.9+:** Required for the FastAPI backend.
    *   [Python Download](https://www.python.org/downloads/)
*   **pip (Python Package Installer):** Usually comes with Python.
*   **Git:** For cloning the repository.
    *   [Git Download](https://git-scm.com/downloads)

## Setup Steps

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/dunamismax/dunamismax.git
    cd dunamismax
    ```

2.  **Frontend Setup (Next.js)**

    Navigate to the `frontend` directory and install the dependencies:

    ```bash
    cd frontend
    npm install
    ```

3.  **Backend Setup (FastAPI)**

    Open a new terminal, navigate to the `backend` directory, and install the Python dependencies. It's highly recommended to use a virtual environment.

    ```bash
    cd ../backend
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

    **Note:** You will need to configure your Supabase environment variables in a `.env` file in the `backend` directory. Copy the `.env.example` file and fill in your actual Supabase URL and key.

    ```bash
    cp .env.example .env
    # Open .env and add your Supabase credentials
    ```

## Running the Application

To run the full application, you will need to start both the frontend and backend servers concurrently.

1.  **Start the Backend Server (FastAPI)**

    In the `backend` directory (where you activated your virtual environment):

    ```bash
    uvicorn main:app --reload
    ```

    This will start the FastAPI server, typically on `http://127.0.0.1:8000`.

2.  **Start the Frontend Server (Next.js)**

    Open a **new terminal**, navigate to the `frontend` directory:

    ```bash
    cd ../frontend
    npm run dev
    ```

    This will start the Next.js development server, typically on `http://localhost:3000`.

    The Next.js application will automatically proxy API requests to the FastAPI backend.

## Accessing the Website

Once both servers are running, open your web browser and navigate to:

`http://localhost:3000`

You should see the `dunamismax.com` website.

## Stopping the Application

To stop both servers, go to each terminal where they are running and press `Ctrl + C`.
