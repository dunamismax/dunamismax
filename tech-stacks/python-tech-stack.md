# Python Tech Stack

Last reviewed: 2026-03-30

## Best Fit

Use this stack when the project is mostly:

- backend services and APIs
- automation, scripting, and operational tools
- data processing, ingestion, and analysis
- background jobs and integration glue
- CLI utilities where a Python runtime is acceptable
- application logic where development speed and ecosystem depth matter more than a single static binary

Python is not the universal default backend. Use it when the backend shape fits Python. Choose Go when the product is really about networking, daemons, systems work, concurrency, or runtime performance.

For browser frontends, do **not** default to a Python template stack. The default web frontend for this workspace now lives in [web-frontend-tech-stack.md](./web-frontend-tech-stack.md): TypeScript + Bun + Astro + Vue.

## Opinionated Default

| Area | Default |
| --- | --- |
| Python version | Latest stable, 3.12+ |
| Package and env management | `uv` |
| Project manifest | `pyproject.toml` as the single source of truth |
| Linting | `ruff check` |
| Formatting | `ruff format` |
| Type checking | Pyright |
| Testing | pytest + coverage.py |
| Local gates | pre-commit |
| CI | `uv sync` → `ruff` → `pyright` → `pytest` |

## Backend and API Stack

| Area | Default |
| --- | --- |
| API framework | FastAPI |
| Validation | Pydantic v2 |
| Config | pydantic-settings |
| Database | PostgreSQL via SQLAlchemy 2.0 by default; SQLite only when deliberately local-first, embedded, cache-like, or tiny |
| Migrations | Alembic |
| HTTP client | HTTPX |
| ASGI server | Uvicorn |
| Background work | Plain process or queue only when the repo actually needs it |
| Browser frontend pairing | Astro + Vue on Bun |
| Terminal frontend pairing | OpenTUI + TypeScript + Bun |

FastAPI stays in the stack, but now as a backend and API tool, not the default browser frontend story.

## Backend Role

In this workspace, Python is the default choice when the backend problem looks like this:

- API orchestration
- automation and scripting
- data work
- backend service logic
- integrations and adapters
- internal tools with moderate runtime demands
- jobs, workers, importers, and admin tooling

If the product also needs a browser surface, the browser frontend should usually be a separate Astro + Vue app consuming the Python API or sharing same-origin boundaries through a thin integration layer.

If the product also needs a terminal operator surface, pair the Python backend with OpenTUI instead of trying to cram terminal UX into a plain CLI.

## Golden Path

1. Start with `uv init` and a clean `pyproject.toml`.
2. Pin the Python version in `.python-version`.
3. Add `ruff` and `pyright` from day one.
4. Use type hints everywhere. No untyped public functions.
5. Start with PostgreSQL unless the repo is intentionally local-first or embedded.
6. Use `pytest` for tests and keep them close to the code or under `tests/`.
7. Use `uv run` for scripts and `uv sync` for dependency management.
8. Keep the browser frontend separate when the product has a real web surface.

## Default Repo Shape

### Libraries, automation, and service code

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

### FastAPI backend

```text
project/
  src/
    app/
      __init__.py
      main.py
      api/
      services/
      models/
      db/
      config.py
  tests/
  migrations/
  alembic.ini
  pyproject.toml
  .python-version
  README.md
```

Keep templates and static browser assets out of the Python repo unless the repo has a deliberate, documented reason to serve them directly.

## Dependency Rules

- Use `uv add` for dependencies. Do not hand-edit dependency lists unless there is a good reason.
- Lock dependencies with `uv lock`. Commit the lockfile.
- Separate runtime and dev dependencies.
- Prefer well-maintained packages with type stubs or inline types.
- Avoid dependency sprawl. The standard library covers a lot.

## Testing Guidance

- Use `pytest` for everything.
- Use `pytest-cov` for coverage reporting.
- Use fixtures over setup and teardown methods.
- Use `httpx` and FastAPI testing utilities for API tests.
- Test the API contract, not just individual functions.

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

- Validate inputs with Pydantic.
- Use environment variables for secrets. Never commit `.env` files.
- Use `bandit` when the repo handles sensitive data or untrusted execution paths.
- Pin dependencies and audit regularly.
- Put explicit timeouts on outbound network calls.

## When Not To Use Python

- high-concurrency network services or daemons where Go is the better runtime
- single-binary operator tools that need zero-runtime distribution
- systems work where deployment simplicity and concurrency dominate the trade
- browser frontend implementation
- rich terminal UI-first products where OpenTUI is the actual fit

## Avoid By Default

- Django
- Poetry
- pipenv
- `setup.py` or `setup.cfg` for new repos
- Black + isort + flake8 when ruff replaces them
- mypy when Pyright is already in the stack
- Python template-driven browser frontends as the default web path
- mixing frontend concerns into the Python repo without a clear reason
