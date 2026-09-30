# 📜 LegalEase - Demo Video Script & Production Guide

> **Project:** LegalEase - AI-Powered Legal Document Generator  
> **Total Estimated Duration:** ~4 to 5 Minutes  
> **Format:** Audio-Visual Screen Recording & Code Walkthrough Script  
> **Target Audience:** Developers, LegalTech Innovators, & Solution Architects  

---

## ⏱️ Master Video Time Budget

| Section | Target Duration | Description |
| :--- | :--- | :--- |
| **1. Intro Hook & Project Overview** | 20 Seconds | Project purpose, high-level architecture & AI capabilities. |
| **2. Codebase Deep Dive (9 Files)** | 2 Minutes (~12-15s / file) | Explanation of every core Python source file in the repository. |
| **3. Web Dashboard Demo** | 1 Minute 45 Seconds | Live interactive demonstration of UI, generation, editing & export. |
| **4. Outro & Conclusion** | 15 Seconds | Wrap-up, key takeaways, and call to action. |

---

## 🎬 Section 1: Introduction & Project Overview (0:00 - 0:20)

* **Visual:** Full-screen title card with the LegalEase logo and dynamic background.
* **Audio Script:**  
  > *"Welcome to LegalEase — an AI-powered legal document generation platform. LegalEase streamlines contract creation by leveraging Google Gemini AI, FastAPI backend microservices, and a Streamlit dashboard. In this video, we'll walk through every single code file in the repository for 10 to 15 seconds, followed by a live demonstration of the interactive web dashboard."*

---

## 💻 Section 2: Codebase Walkthrough (0:20 - 2:20)

*Each code file is presented with on-screen code highlights, key functions, and a strict 10–15 second explanation.*

---

### 📄 1. [`config.py`](file:///c:/Users/LENOVO/Desktop/legalEase/config.py)
* **Timestamp:** 0:20 - 0:33 *(13 seconds)*
* **Visual On-Screen:** Highlight lines 12–25 (Backend URLs, Gemini model settings, asset paths).
* **Speaker Script:**  
  > *"Starting with [`config.py`](file:///c:/Users/LENOVO/Desktop/legalEase/config.py), this central configuration module sets up environment variables using `python-dotenv`. It defines backend host ports, Gemini AI model selections, directory paths for images and docs, and company branding metadata like legal disclaimers and footers."*
* **Key Code Highlight:** Centralized `GEMINI_MODEL` fallback configuration and dynamic directory creation.

---

### 📄 2. [`generate_logos.py`](file:///c:/Users/LENOVO/Desktop/legalEase/generate_logos.py)
* **Timestamp:** 0:33 - 0:46 *(13 seconds)*
* **Visual On-Screen:** Highlight `make_logos()` function and PIL drawing primitives (lines 8–32).
* **Speaker Script:**  
  > *"Next is [`generate_logos.py`](file:///c:/Users/LENOVO/Desktop/legalEase/generate_logos.py). This script uses the Python Pillow library to programmatically generate transparent high-resolution branding assets. It draws scales-of-justice vector icons and generates both light mode `Logo.png` and dark mode `inverseLogo.png` automatically."*
* **Key Code Highlight:** Programmatic graphics generation with PIL `ImageDraw` arcs and text styling.

---

### 📄 3. [`run_all.py`](file:///c:/Users/LENOVO/Desktop/legalEase/run_all.py)
* **Timestamp:** 0:46 - 0:59 *(13 seconds)*
* **Visual On-Screen:** Highlight `start_services()` subprocess calls (lines 9–21).
* **Speaker Script:**  
  > *"`[run_all.py](file:///c:/Users/LENOVO/Desktop/legalEase/run_all.py)` acts as our multi-service orchestrator. Utilizing Python's `subprocess` module, it concurrently boots up the FastAPI backend on port 8000 and the Streamlit frontend dashboard on port 8501, handling graceful shutdowns when interrupted."*
* **Key Code Highlight:** Async process coordination with `subprocess.Popen` and `KeyboardInterrupt` handling.

---

### 📄 4. [`app.py` (Root)](file:///c:/Users/LENOVO/Desktop/legalEase/app.py)
* **Timestamp:** 0:59 - 1:12 *(13 seconds)*
* **Visual On-Screen:** Highlight Streamlit layout and direct Gemini API call (lines 20–55).
* **Speaker Script:**  
  > *"The root `[app.py](file:///c:/Users/LENOVO/Desktop/legalEase/app.py)` serves as a standalone lightweight Streamlit interface. It includes localized UI controls in Tamil and connects directly to the Google GenAI SDK to generate agreements with disclaimers when running in single-tier mode."*
* **Key Code Highlight:** Streamlit sidebar form inputs and direct Google GenAI client integration.

---

### 📄 5. [`ai_core/gemini_generator.py`](file:///c:/Users/LENOVO/Desktop/legalEase/ai_core/gemini_generator.py)
* **Timestamp:** 1:12 - 1:26 *(14 seconds)*
* **Visual On-Screen:** Highlight candidate models list and `_generate_fallback` method (lines 28–46).
* **Speaker Script:**  
  > *"In `[ai_core/gemini_generator.py](file:///c:/Users/LENOVO/Desktop/legalEase/ai_core/gemini_generator.py)`, we encapsulate the core AI document engine. It features auto-retry across model candidates—`gemini-3.8-flash`, `3.6-flash`, and `2.5-flash`—and includes a deterministic legal fallback generator if API quotas are exceeded."*
* **Key Code Highlight:** Multi-model AI fallbacks and deterministic offline contract synthesis engine.

---

### 📄 6. [`ai_core/generator.py`](file:///c:/Users/LENOVO/Desktop/legalEase/ai_core/generator.py)
* **Timestamp:** 1:26 - 1:40 *(14 seconds)*
* **Visual On-Screen:** Highlight `format_docx`, `format_pdf`, and `format_html_preview` functions.
* **Speaker Script:**  
  > *"`[ai_core/generator.py](file:///c:/Users/LENOVO/Desktop/legalEase/ai_core/generator.py)` is our document layout and exporter engine. It sanitizes text, generates formatted `.docx` files using `python-docx`, renders PDF documents complete with headers and page numbering via `FPDF`, and creates styled dark-mode HTML previews."*
* **Key Code Highlight:** Multi-format document compilation (`.docx`, `.pdf`, `.html`) with custom typography and headers.

---

### 📄 7. [`legalEaseAPI/main.py`](file:///c:/Users/LENOVO/Desktop/legalEase/legalEaseAPI/main.py)
* **Timestamp:** 1:40 - 1:53 *(13 seconds)*
* **Visual On-Screen:** Highlight FastAPI app initialization and route registration (lines 13–21).
* **Speaker Script:**  
  > *"Moving to [`legalEaseAPI/main.py`](file:///c:/Users/LENOVO/Desktop/legalEase/legalEaseAPI/main.py), this is the entry point for our FastAPI backend microservice. It initializes the FastAPI application, sets sys.path resolution for the root package, registers route endpoints, and configures the Uvicorn server."*
* **Key Code Highlight:** Uvicorn ASGI server initialization and modular APIRouter mounting.

---

### 8. [`legalEaseAPI/routes.py`](file:///c:/Users/LENOVO/Desktop/legalEase/legalEaseAPI/routes.py)
* **Timestamp:** 1:53 - 2:06 *(13 seconds)*
* **Visual On-Screen:** Highlight `DocumentRequest` Pydantic model and `/generate` endpoint (lines 8–27).
* **Speaker Script:**  
  > *"`[legalEaseAPI/routes.py](file:///c:/Users/LENOVO/Desktop/legalEase/legalEaseAPI/routes.py)` defines our REST API endpoints. It validates incoming request payloads like document types, parties, terms, and dates using Pydantic schema models, delegating legal document creation to the AI engine."*
* **Key Code Highlight:** Request validation with Pydantic `BaseModel` and `/generate` POST handler.

---

### 📄 9. [`frontend/app.py`](file:///c:/Users/LENOVO/Desktop/legalEase/frontend/app.py)
* **Timestamp:** 2:06 - 2:20 *(14 seconds)*
* **Visual On-Screen:** Highlight custom CSS styling, API request POST call, and download buttons (lines 24–48, 80–105).
* **Speaker Script:**  
  > *"Finally, [`frontend/app.py`](file:///c:/Users/LENOVO/Desktop/legalEase/frontend/app.py) powers the primary web application dashboard. Built with Streamlit and styled with custom CSS dark-mode glassmorphism, it manages user input forms, session state, real-time backend API requests, inline contract editing, and instant download buttons."*
* **Key Code Highlight:** Streamlit session state management, responsive dark mode CSS, and REST API client integration.

---

## 🖥️ Section 3: Web Dashboard Showcase (2:20 - 4:05)

*A comprehensive 1 Minute 45 Second live walkthrough of the running LegalEase web dashboard.*

---

### 🎨 Scene 1: Dashboard Overview & Visual Aesthetics (2:20 - 2:40 | 20 seconds)
* **Visual Action:** Open browser to `http://localhost:8501`. Mouse cursor hovers over the custom inverted dark logo `inverseLogo.png` and the sleek dark layout container.
* **Speaker Script:**  
  > *"Now let me show you the live LegalEase web dashboard. Notice the dark-themed UI built with custom CSS, showcasing our dynamically generated scales-of-justice logo. The clean centered layout ensures an intuitive experience for legal professionals and business users alike."*

---

### 📝 Scene 2: Parameter Entry & Input Customization (2:40 - 3:05 | 25 seconds)
* **Visual Action:** Type inputs in the form:
  * **Document Type:** `Freelance Work Contract`
  * **Parties Involved:** `Jane Doe (Service Provider), TechNova Inc. (Client)`
  * **Terms & Conditions:** `Work must be delivered by May 15, 2025; Payment will be made within 7 days of invoice; The client retains Intellectual property rights; Confidentiality must be maintained at all times;`
  * **Effective Date:** `April 15, 2025`
* **Speaker Script:**  
  > *"On the main dashboard, users enter key agreement parameters. Here we specify the Document Type, involved parties, effective start date, and key terms separated by semicolons. Semicolons are automatically transformed into structured legal clauses by our backend processing pipeline."*

---

### ⚡ Scene 3: Live AI Generation & HTML Legal Preview (3:05 - 3:35 | 30 seconds)
* **Visual Action:** Click the **"Generate Document"** button. The spinner runs briefly ("Generating legal document with AI..."). The generated contract appears in an HTML preview container with blue titles, bold headings, and numbered sections.
* **Speaker Script:**  
  > *"When we click 'Generate Document', the frontend transmits a REST payload to our FastAPI backend, triggering Gemini AI. Within seconds, a complete, legally structured contract appears in a styled HTML card. Notice the clear section headings, formal WITNESSETH preambles, structured clauses, and signature block placeholders."*

---

### ✏️ Scene 4: Interactive Document Editor & Multi-Format Export (3:35 - 4:05 | 30 seconds)
* **Visual Action:** 
  1. Click **"✏️ Click to Edit Document"**. An editable text area expands. Make a quick text modification (e.g. edit payment terms or add a custom clause).
  2. Click **"📄 Download as .TXT"**, **"📝 Download as .DOCX"**, and **"📕 Download as .PDF"**.
  3. Briefly switch screen to open the downloaded `.DOCX` file showing embedded logo and footer, and `.PDF` showing page numbers.
* **Speaker Script:**  
  > *"LegalEase gives users complete control. Clicking 'Click to Edit Document' opens an inline editor allowing instant modifications before finalizing. Once satisfied, users can download their document in three formats with a single click: plain text `.TXT`, Microsoft Word `.DOCX` with embedded letterhead logos and footers, or publication-ready `.PDF`."*

---

## 🎯 Section 4: Outro & Summary (4:05 - 4:20)

* **Visual:** Return to main dashboard view with completed document and download options highlighted.
* **Speaker Script:**  
  > *"That completes our tour of LegalEase — from modular backend APIs and AI core generators to a seamless, full-featured legal document dashboard. Thank you for watching!"*

---

## 📌 Production & Recording Instructions

1. **Screen Resolution:** 1920x1080 (1080p, 60fps recommended).
2. **IDE Theme:** Dark theme (e.g., VS Code Dark+ / One Dark Pro) matching the dashboard aesthetic.
3. **Services Pre-Check:** Run `python run_all.py` prior to recording to ensure FastAPI on `:8000` and Streamlit on `:8501` are active and responsive.
