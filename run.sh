#!/bin/bash
# LegalEase Launcher Script
echo "Starting FastAPI Backend..."
python -m uvicorn legalEaseAPI.main:app --host 127.0.0.1 --port 8000 --reload &

sleep 2

echo "Starting Streamlit Frontend..."
streamlit run frontend/app.py --server.port 8501
