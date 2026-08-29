# Genus Website

<div align="center">

![Genus Core](https://img.shields.io/badge/Genus-Core%20Web%20UI-blueviolet?style=for-the-badge)
![Django](https://img.shields.io/badge/Django-5.2-green?style=for-the-badge&logo=django)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-teal?style=for-the-badge&logo=fastapi)
![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)

</div>

---

## 📖 Introduction

**Genus Website** (`genus_web`) is a robust, hybrid-architecture web application designed specifically to serve **Genus Core** through a clean, modern, and high-performance Web UI. Built combining the power of **Django** for robust MVC modeling and server-side templates, alongside **FastAPI** mounted seamlessly via **Starlette ASGI routing**, this repository bridges the gap between traditional web frameworks and lightning-fast asynchronous API endpoints.

Whether you're managing background agent routines, inspecting database configurations, or integrating custom UI workflows, Genus Website acts as the centralized control panel and web interface for the Genus ecosystem.

---

## ⚙️ Core Architecture & Tech Stack

The application leverages a dual-framework ASGI approach to handle synchronous and asynchronous requests under a single unified server instance:

*   **ASGI Server**: Powered by **Uvicorn** with hot-reload capabilities and colored logging via **Colorama**.
*   **Routing & ASGI Aggregation**: Uses **Starlette** to mount FastAPI under `/api/v1` and Django under `/` (root paths).
*   **Backend Framework (MVC)**: **Django 5.2**, configured with modular apps, robust middleware stack, and custom management tools.
*   **API Framework**: **FastAPI** for high-performance, asynchronous REST endpoints (`/api/v1`).
*   **Database Integration**: Flexible database connectivity via `dj-database_url` supporting external PostgreSQL/relational databases alongside standard Django ORM capabilities.
*   **Static Asset Management**: Integrated **WhiteNoise** middleware with compressed manifest static files storage for optimum production asset caching.
*   **AI Integration**: Pre-configured support for **Google GenAI SDK** (`google-genai`), `pydantic`, and environment management utilities (`python-dotenv`).

---

## 📂 Project Directory Structure

```tree
genus_web/
├── .env                     # Environment variables configuration
├── .genus/                  # Genus internal configuration & metadata
├── .git/                    # Git version control repository
├── .gitignore               # Ignored files and directories
├── .venv/                   # Python virtual environment
├── api/                     # FastAPI module
│   └── main.py              # FastAPI application initialization & routers
├── app/                     # Main Django application module
│   ├── admin.py             # Django admin site registrations
│   ├── apps.py              # App configuration descriptor
│   ├── migrations/          # Database migration history
│   ├── models.py            # Django ORM data models
│   ├── tests.py             # Unit and integration test suites
│   ├── urls.py              # App-specific URL dispatcher
│   └── views.py             # Request handlers (Home, Favicon, etc.)
├── credentials.json         # Google API service credentials
├── drive_token.json         # Google Drive OAuth token store
├── manage.py                # Django command-line utility
├── requirements.txt         # Project Python dependencies list
├── server.py                # Primary server entrypoint script (Uvicorn)
├── static/                  # Global static assets (CSS, JS, Favicon)
├── templates/               # Global HTML template directory
└── web/                     # Django project configuration package
    ├── asgi.py              # ASGI routing bridge (Starlette + Django + FastAPI)
    ├── settings.py          # Django project settings & environment bindings
    ├── urls.py              # Global project URL configurations
    └── wsgi.py              # Legacy WSGI entrypoint
```

---

## 🚀 Getting Started & Installation

### Prerequisites
*   Python 3.10+ installed on your system.
*   An active virtual environment (e.g., `.venv`).

### 1. Clone the Repository & Navigate
```bash
git clone https://github.com/plusstudiocorp/Genus-Agent.git
cd genus_web
```

### 2. Activate Virtual Environment
On Windows (Command Prompt / PowerShell):
```cmd
.venv\Scripts\activate
```

On Unix / macOS:
```bash
source .venv/bin/activate
```

### 3. Install Dependencies
Ensure all required libraries specified in `requirements.txt` are installed:
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create or modify your `.env` file in the root directory with the necessary parameters:
```env
HOST=0.0.0.0
PORT=80
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DB1_URL=sqlite:///db.sqlite3
```

---

## 💻 Running the Server

You can launch the server using the dedicated entrypoint script:

```bash
python server.py
```

This initializes Uvicorn with auto-reload enabled, binding to your configured `HOST` and `PORT` (defaulting to `0.0.0.0:80`), serving both the FastAPI routes (`/api/v1`) and Django web application concurrently.

Alternatively, standard Django management commands can be utilized:
```bash
python manage.py runserver
```

---

## 🔌 API Endpoints & Routing Overview

*   **`GET /`**: Main Django web response (`Hello!` / Genus Core UI view).
*   **`GET /favicon.ico`**: Dynamic favicon file response handler.
*   **`GET /api/v1/`**: FastAPI root endpoint (expandable for high-speed agent queries and JSON payloads).
*   **Django Admin**: Configurable via `web/urls.py` and `app/admin.py`.

---

## 🛠️ Development & Maintenance

*   **Database Migrations**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
*   **Static Files Collection**:
    ```bash
    python manage.py collectstatic
    ```

---

## 📄 License

This repository is proprietary software developed by **PlusStudio Corp**. All rights reserved.
