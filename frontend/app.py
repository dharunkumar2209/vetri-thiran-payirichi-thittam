import sys
from pathlib import Path

# Add project root to sys.path
root_dir = Path(__file__).resolve().parent.parent
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

import streamlit as st
import requests
from config import BACKEND_URL, LOGO_PATH, INVERSE_LOGO_PATH
from ai_core.generator import sanitize_text, format_docx, format_pdf, format_html_preview
from ai_core.gemini_generator import GeminiDocumentGenerator

# Page Configuration
st.set_page_config(
    page_title="LegalEase",
    page_icon="⚖️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom Styling
st.markdown("""
<style>
    .main {
        background-color: #0b0f19;
    }
    .stButton > button {
        width: 100%;
        background-color: #2563eb;
        color: white;
        border-radius: 6px;
        padding: 10px 20px;
        font-weight: 600;
        border: none;
    }
    .stButton > button:hover {
        background-color: #1d4ed8;
    }
    div[data-testid="stForm"] {
        border: 1px solid #1e293b;
        background-color: #0f172a;
        padding: 20px;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Logo & Header Layout
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if INVERSE_LOGO_PATH.exists():
        st.image(str(INVERSE_LOGO_PATH), use_container_width=True)
    elif LOGO_PATH.exists():
        st.image(str(LOGO_PATH), use_container_width=True)
    else:
        st.markdown("<h1 style='text-align: center;'>⚖️ LegalEase</h1>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center; color: #94a3b8; font-weight: 400; margin-bottom: 25px;'>AI Legal Document Generator</h3>", unsafe_allow_html=True)

# User Inputs Form
with st.container():
    document_type = st.text_input("Document Type (Ex: Agreement, Contract, NDA)", value="Freelance Work Contract")
    parties = st.text_area("Parties Involved", value="Jane Doe (Service Provider), TechNova Inc. (Client)")
    terms = st.text_area("Terms & Conditions (Use semicolons for bullet points)", value="Work must be delivered by May 15, 2025;\nPayment will be made within 7 days of invoice;\nThe client retains Intellectual property rights;\nConfidentiality must be maintained at all times;", height=120)
    dates = st.text_input("Effective Date", value="April 15, 2025")

    generate_btn = st.button("Generate Document")

# Session state initialization
if "generated_text" not in st.session_state:
    st.session_state.generated_text = ""
if "show_edit" not in st.session_state:
    st.session_state.show_edit = False

# Document Generation Logic
if generate_btn:
    with st.spinner("Generating legal document with AI..."):
        try:
            # Send POST request to backend API
            payload = {
                "document_type": document_type,
                "parties": parties,
                "terms": terms,
                "dates": dates
            }
            api_endpoint = f"{BACKEND_URL}/generate"
            res = requests.post(api_endpoint, json=payload, timeout=20)
            
            if res.status_code == 200:
                doc_content = res.json().get("document", "")
            else:
                # Direct AI generator fallback if backend endpoint returns non-200
                generator = GeminiDocumentGenerator()
                doc_content = generator.generate_document(document_type, parties, terms, dates)
        except Exception:
            # Direct AI generator fallback if network call to backend fails
            generator = GeminiDocumentGenerator()
            doc_content = generator.generate_document(document_type, parties, terms, dates)

        st.session_state.generated_text = sanitize_text(doc_content)
        st.session_state.show_edit = False
        st.success("Document Generated Successfully!")

# Display & Preview Section
if st.session_state.generated_text:
    st.markdown("---")
    
    # Styled HTML Preview
    styled_preview = format_html_preview(st.session_state.generated_text)
    st.markdown(styled_preview, unsafe_allow_html=True)

    st.markdown("")
    
    # Toggle Edit Button
    if st.button("✏️ Click to Edit Document"):
        st.session_state.show_edit = not st.session_state.show_edit

    # Editable Text Area
    if st.session_state.show_edit:
        st.markdown("#### Edit Document Below:")
        edited_text = st.text_area(
            "Document Content",
            value=st.session_state.generated_text,
            height=300,
            key="document_editor"
        )
        st.session_state.generated_text = edited_text

    st.markdown("### Download Options")
    file_prefix = document_type.lower().replace(" ", "_")

    col_txt, col_docx, col_pdf = st.columns(3)

    with col_txt:
        st.download_button(
            label="📄 Download as .TXT",
            data=st.session_state.generated_text,
            file_name=f"{file_prefix}.txt",
            mime="text/plain",
            use_container_width=True
        )

    with col_docx:
        docx_bytes = format_docx(st.session_state.generated_text, document_type)
        st.download_button(
            label="📝 Download as .DOCX",
            data=docx_bytes,
            file_name=f"{file_prefix}.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            use_container_width=True
        )

    with col_pdf:
        pdf_bytes = format_pdf(st.session_state.generated_text, document_type)
        st.download_button(
            label="📕 Download as .PDF",
            data=pdf_bytes,
            file_name=f"{file_prefix}.pdf",
            mime="application/pdf",
            use_container_width=True
        )
