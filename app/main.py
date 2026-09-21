from fastapi import FastAPI

app = FastAPI(
    title="DeployFlow",
    description="A small service for demonstrating deployment and DevOps",
    version="1.0.1",
)


@app.get("/")
def home():
    return {
        "project": "DeployFlow",
        "message": "Service is running",
    }


@app.get("/health")
def health():
    return {"status": "ok"}