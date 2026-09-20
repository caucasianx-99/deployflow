# DeployFlow — Docker, CI & Cloud Deployment

DeployFlow is an independent DevOps portfolio project demonstrating how to package, test, and deploy a small Python web service.

The focus is on containerization, Linux-based CI, automated health checks, and public cloud deployment—not application complexity.

## Live Demo

- Service: https://deployflow-5by1.onrender.com/
- Health check: https://deployflow-5by1.onrender.com/health
- API documentation: https://deployflow-5by1.onrender.com/docs

The service runs on Render's free instance, which may take time to wake up after inactivity.

## Technology

Python · FastAPI · Docker · Linux containers · GitHub Actions · Render · pytest

## Features

- FastAPI service with a health-check endpoint
- Docker image based on Python 3.12
- Application runs as a non-root container user
- Automated endpoint tests with pytest
- GitHub Actions CI on pushes and pull requests
- CI builds and starts the Docker container
- Health-check retries during container startup
- Public deployment on Render using the Dockerfile

## Run Locally

Create a virtual environment:

```bash
python -m venv .venv
```

Install development dependencies:

```bash
python -m pip install -r requirements-dev.txt
```

Run tests:

```bash
python -m pytest -q
```

Start the service:

```bash
python -m uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/docs.

## Docker

Build the image:

```bash
docker build -t deployflow:local .
```

Start the container:

```bash
docker run --rm -p 8000:8000 deployflow:local
```

Check http://127.0.0.1:8000/health.

## CI Pipeline

The GitHub Actions workflow:

1. Checks out the repository.
2. Installs Python dependencies.
3. Runs automated tests.
4. Builds the Docker image on a Linux runner.
5. Starts the container and checks `/health`, retrying while the service starts.

Workflow: [.github/workflows/ci.yml](.github/workflows/ci.yml)

## Deployment

DeployFlow is hosted on Render as a Docker web service connected to this GitHub repository.

The public service is a demonstration. It does not include a database, user authentication, persistent storage, or a production availability guarantee.