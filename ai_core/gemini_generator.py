import os
import google.generativeai as genai
from config import GEMINI_API_KEY, GEMINI_MODEL

class GeminiDocumentGenerator:
    def __init__(self, model_name: str = None):
        self.model_name = model_name or GEMINI_MODEL or "gemini-3.8-flash"
        self.api_key = GEMINI_API_KEY or os.getenv("GEMINI_API_KEY", "")
        if self.api_key and not self.api_key.startswith("YOUR_"):
            try:
                genai.configure(api_key=self.api_key)
            except Exception as e:
                print(f"[Warning] Failed to configure Gemini API key: {e}")

    def generate_document(self, document_type: str, parties: str, terms: str, dates: str) -> str:
        prompt = (
            f"Generate a comprehensive, legally sound legal document titled '{document_type}'.\n\n"
            f"Involved Parties:\n{parties}\n\n"
            f"Effective Date: {dates}\n\n"
            f"Key Terms and Covenants:\n{terms}\n\n"
            f"Requirements:\n"
            f"1. Include formal legal preamble (WITNESSETH, WHEREAS, NOW THEREFORE).\n"
            f"2. Organize into numbered sections (e.g. 1. Scope of Agreement, 2. Terms and Conditions, 3. Compensation & Payment, 4. Confidentiality, 5. Term & Termination, 6. Governing Law, 7. Entire Agreement).\n"
            f"3. Include signature block placeholders for all parties.\n"
            f"4. Do NOT use markdown code block backticks (like ```markdown), output clean raw markdown document text directly."
        )

        candidate_models = [self.model_name, "gemini-3.8-flash", "gemini-3.6-flash", "gemini-2.5-flash"]
        unique_candidates = []
        for m in candidate_models:
            if m and m not in unique_candidates:
                unique_candidates.append(m)

        if self.api_key and not self.api_key.startswith("YOUR_"):
            for m_name in unique_candidates:
                try:
                    model_inst = genai.GenerativeModel(m_name)
                    response = model_inst.generate_content(prompt)
                    if response and hasattr(response, "text") and response.text:
                        cleaned_text = response.text.replace("```markdown", "").replace("```", "").strip()
                        return cleaned_text
                except Exception as e:
                    print(f"[Warning] Gemini API call error with model '{m_name}': {e}")

        # Fallback structured legal document generator if API is unavailable or quota exceeded
        return self._generate_fallback(document_type, parties, terms, dates)

    def _generate_fallback(self, document_type: str, parties: str, terms: str, dates: str) -> str:
        term_items = [t.strip() for t in terms.replace("\n", ";").split(";") if t.strip()]
        formatted_terms = "\n".join([f"{i+1}. {t}" for i, t in enumerate(term_items)]) if term_items else "1. Standard operational and compliance terms shall apply."
        
        return (
            f"## {document_type}\n\n"
            f"Agreement made this {dates}\n\n"
            f"Between:\n\n"
            f"{parties}\n\n"
            f"WITNESSETH:\n\n"
            f"WHEREAS, the parties desire to enter into this {document_type} to define their rights, responsibilities, and covenants;\n\n"
            f"NOW, THEREFORE, in consideration of the mutual covenants herein contained, the parties agree as follows:\n\n"
            f"1. Scope of Agreement:\n"
            f"This Agreement sets forth the complete terms and conditions under which the services, obligations, and deliverables shall be executed between the parties.\n\n"
            f"2. Terms and Conditions:\n"
            f"{formatted_terms}\n\n"
            f"3. Term and Termination:\n"
            f"This Agreement shall commence on {dates} and shall continue until completed or terminated by either party upon giving fifteen (15) days written notice.\n\n"
            f"4. Confidentiality:\n"
            f"Each party acknowledges and agrees that all confidential or proprietary information shared during the performance of this Agreement shall remain strictly confidential.\n\n"
            f"5. Independent Relationship:\n"
            f"Nothing in this Agreement shall be construed as creating an agency, partnership, or employment relationship between the parties.\n\n"
            f"6. Governing Law & Jurisdiction:\n"
            f"This Agreement shall be governed by and construed in accordance with the laws of the applicable jurisdiction.\n\n"
            f"7. Entire Agreement:\n"
            f"This Agreement constitutes the entire understanding between the parties with respect to the subject matter hereof and supersedes all prior agreements.\n\n"
            f"IN WITNESS WHEREOF, the parties hereto have executed this {document_type} as of {dates}."
        )
