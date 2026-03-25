# Python Tech Stack

Last reviewed: 2026-03-25

## Best Fit

Use this stack when the project is mostly:

- automation, scripting, and operational tools
- CLI utilities and data processing
- API services and backend systems
- web applications with server-rendered frontends
- anything where development speed and ecosystem depth matter more than binary size

Python is the default for new tools, scripts, automation, APIs, and web surfaces. Use Go when the product needs a single-binary deploy, high-concurrency networking, or systems-level performance. Use Rust only when the project genuinely needs it.

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

## Web Stack

| Area | Default |
| --- | --- |
| Framework | FastAPI |
| Validation | Pydantic v2 |
| Config | pydantic-settings |
| Database (web apps) | PostgreSQL via SQLAlchemy 2.0 |
| Database (local tools) | SQLite |
| Migrations | Alembic |
| HTTP client | HTTPX |
| Server | Uvicorn |
| Templates | Jinja2 |
| Frontend interactivity | htmx + Alpine.js |
| E2E tests | Playwright for Python |

FastAPI is the only Python web framework in this stack. No Django.

### Server-Rendered Frontends

When the product needs a browser surface:

- FastAPI serves Jinja2 templates directly
- htmx handles dynamic updates without a JavaScript build step
- Alpine.js handles small client-side interactions
- No separate frontend build toolchain. No Node, no Bun, no TypeScript, no SPA framework.

This applies to standalone Python web apps and to operator UIs for Go backend products. The Python layer handles templates and rendering; the Go layer handles the core product logic and data.

## Golden Path

1. Start with `uv init` and `pyproject.toml`.
2. Pin Python version in `.python-version`.
3. Add `ruff` and `pyright` to dev dependencies from day one.
4. Use type hints everywhere. No untyped public functions.
5. Use `pytest` for tests. Keep them next to the code or in `tests/`.
6. Set up `pre-commit` with ruff and pyright hooks.
7. Use `uv run` for scripts and `uv sync` for dependency management.

## Default Repo Shape

### Scripts and tools

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

### FastAPI web apps

```text
project/
  src/
    app/
      __init__.py
      main.py
      config.py
      models.py
      routes/
      templates/
      static/
  tests/
  migrations/
  alembic.ini
  pyproject.toml
  .python-version
  README.md
```

## Dependency Rules

- Use `uv add` for dependencies. Never edit `pyproject.toml` dependency lists by hand.
- Lock dependencies with `uv lock`. Commit the lockfile.
- Separate runtime and dev dependencies.
- Prefer well-maintained packages with type stubs or inline types.
- Avoid dependency sprawl. The standard library covers more than most people think.

## Testing Guidance

- Use `pytest` for everything.
- Use `pytest-cov` for coverage reporting.
- Use fixtures over setup/teardown methods.
- Use `httpx` + FastAPI's `TestClient` for API tests.
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

- Validate all inputs with Pydantic.
- Use environment variables for secrets. Never commit `.env` files.
- Use `bandit` for security-focused static analysis when the project handles sensitive data.
- Pin dependencies and audit regularly.

## When Not To Use Python

- Single-binary CLI tools that need zero-dependency distribution → use Go
- High-performance concurrent network services → use Go
- Memory-safety-critical systems code or cargo plugins → use Rust
- Browser-side code → use htmx + Alpine.js from Python templates, not a JS framework

## Avoid By Default

- Django (FastAPI covers all web use cases in this stack)
- Poetry (uv replaces it)
- pipenv (superseded by uv)
- setup.py / setup.cfg (use pyproject.toml)
- Black + isort + flake8 (ruff replaces all three)
- mypy (Pyright is faster and more accurate)
- Flask (use FastAPI)
- React / Vue / Angular / any SPA framework (use server-rendered templates + htmx)
- Node / Bun / TypeScript for frontends (htmx + Alpine.js from Jinja2 templates)
