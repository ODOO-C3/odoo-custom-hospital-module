# Odoo 19 Custom Modules

Custom Odoo modules with Docker-based development and CI/CD.

## Repository Structure

```
your-repo/
├── docker-compose.yml          # Local development
├── docker-compose.test.yml     # CI/CD testing
├── Dockerfile                  # Builds image with modules
├── .dockerignore
├── .gitignore
├── .github/workflows/test.yml  # GitHub Actions
├── my_module/                  # Your module(s)
│   ├── __init__.py
│   ├── __manifest__.py
│   ├── models/
│   └── views/
└── another_module/             # Add more modules as needed
```

## Local Development

```bash
docker compose up -d
```

Open http://localhost:8069, create a database, then install your module from Apps.

- Code changes auto-reload (Python)
- XML/view changes: refresh browser

```bash
docker compose logs -f web     # View logs
docker compose restart web     # Restart Odoo
docker compose down            # Stop
docker compose down -v         # Stop and delete data
```

## Running Tests Locally

```bash
# Test specific module(s)
MODULES=my_module docker compose -f docker-compose.test.yml up --build --abort-on-container-exit

# Cleanup
docker compose -f docker-compose.test.yml down -v
```

## CI/CD

Tests run automatically on push/PR via GitHub Actions.

Edit `.github/workflows/test.yml` to set your module names:

```yaml
env:
  MODULES: my_module,another_module
```

## Scaffolding a New Module

```bash
docker compose exec web odoo scaffold new_module /mnt/extra-addons
```

## For Coworkers

```bash
git clone <repo-url>
docker compose up -d
```