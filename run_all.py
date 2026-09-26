import os
import sys
import time
import subprocess

def start_services():
    print("Starting LegalEase Services...")
    
    # Start FastAPI Backend
    backend_cmd = [sys.executable, "-m", "uvicorn", "legalEaseAPI.main:app", "--host", "127.0.0.1", "--port", "8000", "--reload"]
    print("Launching FastAPI Backend on http://127.0.0.1:8000...")
    backend_process = subprocess.Popen(backend_cmd)
    
    # Wait 2 seconds for backend initialization
    time.sleep(2)
    
    # Start Streamlit Frontend
    frontend_cmd = [sys.executable, "-m", "streamlit", "run", "frontend/app.py", "--server.port", "8501"]
    print("Launching Streamlit Frontend on http://localhost:8501...")
    frontend_process = subprocess.Popen(frontend_cmd)
    
    try:
        backend_process.wait()
        frontend_process.wait()
    except KeyboardInterrupt:
        print("\nStopping services...")
        backend_process.terminate()
        frontend_process.terminate()

if __name__ == "__main__":
    start_services()
