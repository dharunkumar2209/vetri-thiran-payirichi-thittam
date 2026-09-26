import sys
from pathlib import Path

# Add project root to sys.path
root_dir = Path(__file__).resolve().parent.parent
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

from fastapi import FastAPI
from legalEaseAPI.routes import router
from config import BACKEND_HOST, BACKEND_PORT

app = FastAPI(title="LegalEase - AI Legal Document Generator")

# Include routes from routes.py
app.include_router(router)

# Root endpoint
@app.get("/")
def home():
    return {"message": "Welcome to LegalEase AI Legal Document Generator API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("legalEaseAPI.main:app", host=BACKEND_HOST, port=BACKEND_PORT, reload=True)
