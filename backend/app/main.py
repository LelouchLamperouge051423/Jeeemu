from fastapi import FastAPI

app = FastAPI(title="Synapse AI Backend")

@app.get("/")
def root():
    return {"message": "Synapse AI is running"}

@app.get("/health")
def health():
    return {"status": "ok"}