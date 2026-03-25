# Python Tech Stack

Last reviewed: 2026-03-25

## Best Fit

Use this stack when the project is mostly:

- automation, scripting, and operational tools
- CLI utilities and data processing
- API services and backend systems
- full-stack web applications (Django or FastAPI)
- anything where development speed and ecosystem depth matter more than binary size

Python is the default for new tools, scripts, and automation. Use Go when the product needs a single-binary deploy, high-concurrency networking, or systems-level performance. Use Rust only when the project genuinely needs memory safety without GC or cargo-plugin-level ecosystem integration.

## Opinionated Default

| Area | Default |
| --- | --- |
| Python version | Latest stable (3.12+) |
| Package/env management | `uv` |
| Project manifest | `pyproject.toml` (single source of truth) |
| Linting | `ruff check` |
| Formatting | `ruff format` (run `ruff check --fix` first for import sorting) |
| Type checking | Pyright |
| Testing | pytest + coverage.py |
| Local gates | pre-commit |
| CI | `uv sync` → `ruff` → Pyright → `pytest` |

## Web Stack Defaults

### Full-stack (server-rendered)

| Area | Default |
| --- | --- |
| Framework | Django |
| Templates | Django templates + htmx + Alpine.js |
| Database | PostgreSQL (Django's natural fit) |
| ORM | Django ORM |
| Migrations | Django migrations |
| Background jobs | Celery (only when truly needed) |
| Static files | WhiteNoise |

Use Django when the product is a full-stack web application with server-rendered pages. The Django + htmx + Alpine.js combination gives a high Python-to-JavaScript ratio while building modern interactive apps.

### API-first

| Area | Default |
| --- | --- |
| Framework | FastAPI |
| Validation | Pydantic v2 |
| Config | pydantic-settings |
| Database | SQLAlchemy 2.0 + Alembic |
| HTTP client | HTTPX |
| Server | Uvicorn |

Use FastAPI when the backend is the product or when a separate JS/TS frontend dominates. FastAPI + Pydantic v2 is the cleanest modern typed Python API stack.

### Choosing between them

- Start with Django unless you already know you are building an API-first system.
- Use FastAPI when the backend is purely an API layer for a separate frontend.
- Do not mix them in the same project.

## Golden Path

1. Start with `uv init` and `pyproject.toml`.
2. Pin Python version in `.python-version`.
3. Add `ruff` and `pyright` to dev dependencies from day one.
4. Use type hints everywhere. No untyped public functions.
5. Use `pytest` for tests. Keep them next to the code or in `tests/`.
6. Set up `pre-commit` with ruff and pyright hooks.
7. Use `uv run` for scripts and `uv sync` for dependency management.

## Default Repo Shape

```text
project/
  src/
    project_name/
      __init__.py
      main.py
      ...
  tests/
    test_main.py
    ...
  pyproject.toml
  .python-version
  .pre-commit-config.yaml
  README.md
```

For Django projects:

```text
project/
  project_name/
    settings.py
    urls.py
    wsgi.py
  app_name/
    models.py
    views.py
    templates/
    tests/
  manage.py
  pyproject.toml
  .python-version
  README.md
```

## Dependency Rules

- Use `uv add` for dependencies. Never edit `pyproject.toml` dependency lists by hand.
- Lock dependencies with `uv lock`. Commit the lockfile.
- Separate runtime and dev dependencies (`[project.optional-dependencies]` or `[dependency-groups]`).
- Prefer well-maintained packages with type stubs or inline types.
- Avoid dependency sprawl. The standard library covers more than most people think.

## Testing Guidance

- Use `pytest` for everything. No `unittest` unless Django forces it.
- Use `pytest-cov` for coverage reporting.
- Use fixtures over setup/teardown methods.
- Use `httpx` + FastAPI's `TestClient` for API tests.
- Use Django's test client and `pytest-django` for Django tests.
- Use Playwright for Python when end-to-end browser tests are needed.

## CI Quality Bar

Every Python project must pass:

```bash
uv sync
ruff check .
ruff format --check .
pyright
pytest
```

## Security Baseline

- Validate all inputs with Pydantic or Django forms.
- Use environment variables for secrets. Never commit `.env` files.
- Use `bandit` for security-focused static analysis when the project handles sensitive data.
- Pin dependencies and audit regularly.

## When Not To Use Python

- Single-binary CLI tools that need zero-dependency distribution → use Go
- High-performance concurrent network services → use Go
- Memory-safety-critical systems code or cargo plugins → use Rust
- Browser-side code → use TypeScript

## Avoid By Default

- Poetry (uv replaces it with better performance and broader scope)
- pipenv (superseded by uv)
- setup.py / setup.cfg (use pyproject.toml)
- Black + isort + flake8 (ruff replaces all three)
- mypy (Pyright is faster and more accurate for modern Python)
- Flask (use FastAPI for APIs, Django for full-stack)
- SQLite for web apps (use PostgreSQL; SQLite is fine for local CLI tools)
