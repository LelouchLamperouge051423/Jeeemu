from fastapi import FastAPI
from dotenv import load_dotenv
from app.db.supabase import get_supabase_client

load_dotenv()

app = FastAPI(title="Jeeemu", version="0.0.1")

@app.get("/health")
def health():
    return {"status": "ok", "service": "jeeemu"}

@app.get("/db-test")
def test_database():
    try:
        client = get_supabase_client()
        result = client.table("documents").select("id", count="exact").execute()
        return {
            "status": "connected",
            "documents_count": result.count if result.count else 0
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}