import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# .env ஃபைலை லோட் செய்ய
load_dotenv()

st.set_page_config(page_title="LegalEase AI", page_icon="📜", layout="wide")

st.title("📜 LegalEase: AI-Powered Legal Document Generator")
st.write("தேவையான விவரங்களை வழங்கி சட்ட ரீதியான ஆவணங்களை நிமிடங்களில் உருவாக்குங்கள்.")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("Gemini API Key காணப்படவில்லை! `.env` ஃபைலில் GEMINI_API_KEY உள்ளதா எனப் பார்க்கவும்.")
    st.stop()

st.sidebar.header("ஆவண விவரங்கள்")
doc_type = st.sidebar.selectbox(
    "ஆவண வகையைத் தேர்ந்தெடுக்கவும்",
    ["Non-Disclosure Agreement (NDA)", "Employment Contract", "Rent Agreement", "Custom Legal Document"]
)

party_a = st.sidebar.text_input("முதல் தரப்பினர் பெயர் (Party A)", "Company A LLC")
party_b = st.sidebar.text_input("இரண்டாம் தரப்பினர் பெயர் (Party B)", "John Doe")
jurisdiction = st.sidebar.text_input("சட்டம் / மாநிலம் (Jurisdiction)", "India / Tamil Nadu")
extra_details = st.sidebar.text_area("கூடுதல் தகவல்கள் / நிபந்தனைகள்", "Duration: 1 year, Confidentiality period: 2 years.")

if st.button("Generate Legal Document"):
    with st.spinner("Gemini AI ஆவணத்தை உருவாக்கிக்கொண்டிருக்கிறது..."):
        prompt = f"""
        You are an expert legal document generator assistant.
        Generate a formal {doc_type} based on the following details:
        - Party A: {party_a}
        - Party B: {party_b}
        - Jurisdiction/Governing Law: {jurisdiction}
        - Additional Terms: {extra_details}

        Requirements:
        1. Use professional, legally sound language.
        2. Format clearly with headings, bullet points, and numbered clauses.
        3. Include a standard legal disclaimer at the top stating that this document is AI-generated and should be reviewed by a qualified legal professional before use.
        """

        try:
            client = genai.Client(api_key=api_key)
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
            )
            
            st.success("ஆவணம் வெற்றிகரமாக உருவாக்கப்பட்டது!")
            st.markdown("---")
            st.markdown(response.text)

        except Exception as e:
            st.error(f"பிழை ஏற்பட்டது: {e}")


            
