# Odoo 19 Custom Modules

[![Odoo CI/CD](https://github.com/ODOO-C3/odoo-custom-hospital-module/actions/workflows/ci.yml/badge.svg)](https://github.com/ODOO-C3/odoo-custom-hospital-module/actions/workflows/ci.yml)
<!-- COVERAGE_BADGE_START -->
![Coverage](https://img.shields.io/badge/coverage-96%25-green)
<!-- COVERAGE_BADGE_END -->
![Python](https://img.shields.io/badge/python-3.12-blue)

Custom Odoo modules with Docker-based development and CI/CD.

## Repository Structure

```
your-repo/
├── docker-compose.yml          # Local development
├── docker-compose.test.yml     # CI/CD testing with Coverage
├── Dockerfile                  # Builds image with modules
├── requirements.txt            # Python dependencies
├── ruff.toml                   # Linter configuration
├── .dockerignore
├── .gitignore
├── .github/workflows/ci.yml    # Main CI/CD Pipeline
└── placeholder_module/         # Example module
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

## Running Tests & Coverage Locally

```bash
# Run all tests with coverage
docker compose -f docker-compose.test.yml up --build --abort-on-container-exit

# Test specific module(s)
MODULES=placeholder_module docker compose -f docker-compose.test.yml up --build --abort-on-container-exit

# Cleanup
docker compose -f docker-compose.test.yml down -v
```

## CI/CD Pipeline

The pipeline runs automatically on push/PR to `main` or `19.0` branches. It includes:
1. **Linting**: Ruff check and formatting.
2. **Security Scan**: `pip-audit` for dependencies and `Trivy` for the Docker image.
3. **Automated Tests**: Unit tests with a full Odoo environment.
4. **Code Coverage**: Automatic coverage reporting in logs.

## Continuous Deployment (CD)

> [!NOTE]
> Setup CD akan dilakukan apabila sudah diberikan akses VPS oleh partner.

## Scaffolding a New Module

```bash
docker compose exec web odoo scaffold new_module /mnt/extra-addons
```

## For Coworkers

```bash
git clone <repo-url>
docker compose up -d
```