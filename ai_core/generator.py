import re
import io
from pathlib import Path
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls
from fpdf import FPDF
from config import LOGO_PATH, COMPANY_FOOTER, COMPANY_NAME, COMPANY_EMAIL

def sanitize_text(text: str) -> str:
    """Removes special characters and typographic quotes to ensure clean formatting."""
    if not text:
        return ""
    replacements = {
        '“': '"', '”': '"', '‘': "'", '’': "'",
        '—': '-', '–': '-', '•': '*', '…': '...'
    }
    for orig, repl in replacements.items():
        text = text.replace(orig, repl)
    return text

def format_docx(text: str, doc_type: str, logo_path: str = None) -> bytes:
    """Uses python-docx to embed logo, format headings, auto-generate terms table, and footer."""
    doc = Document()
    
    # Page Margins
    for section in doc.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)
        
        # Configure Footer
        footer = section.footer
        p_foot = footer.paragraphs[0]
        p_foot.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        f_run = p_foot.add_run(COMPANY_FOOTER)
        f_run.font.size = Pt(8.5)
        f_run.font.name = 'Times New Roman'
        f_run.font.color.rgb = RGBColor(120, 120, 120)

    # Embed Logo if available
    logo_file = Path(logo_path) if logo_path else LOGO_PATH
    if logo_file and logo_file.exists():
        p_logo = doc.add_paragraph()
        p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo.add_run().add_picture(str(logo_file), width=Inches(2.2))
    
    # Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    t_run = p_title.add_run(doc_type.upper() if doc_type else "LEGAL DOCUMENT")
    t_run.font.name = 'Times New Roman'
    t_run.font.size = Pt(18)
    t_run.font.bold = True
    t_run.font.color.rgb = RGBColor(15, 23, 42)
    p_title.paragraph_format.space_after = Pt(18)

    # Clean text
    clean_txt = sanitize_text(text)
    lines = clean_txt.split('\n')

    in_terms_section = False
    terms_list = []

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
            
        # Remove Markdown header syntax if present
        if stripped.startswith('#'):
            heading_text = stripped.lstrip('#').strip()
            # If it's identical to the main document title, skip redundant title
            if heading_text.lower() == doc_type.lower():
                continue
            p_head = doc.add_paragraph()
            p_head.paragraph_format.space_before = Pt(12)
            p_head.paragraph_format.space_after = Pt(6)
            h_run = p_head.add_run(heading_text)
            h_run.font.name = 'Times New Roman'
            h_run.font.size = Pt(13)
            h_run.font.bold = True
            h_run.font.color.rgb = RGBColor(30, 41, 59)
            continue
            
        # Check for clause headings (e.g., "1. Scope:", "WITNESSETH:", "Between:")
        if re.match(r'^(\d+\.|\b[A-Z\s]{4,}\b|Between:|WITNESSETH:|NOW, THEREFORE,)', stripped):
            p_bold = doc.add_paragraph()
            p_bold.paragraph_format.space_before = Pt(8)
            p_bold.paragraph_format.space_after = Pt(4)
            b_run = p_bold.add_run(stripped)
            b_run.font.name = 'Times New Roman'
            b_run.font.size = Pt(11)
            b_run.font.bold = True
            b_run.font.color.rgb = RGBColor(15, 23, 42)
        else:
            p_body = doc.add_paragraph()
            p_body.paragraph_format.space_after = Pt(6)
            p_body.paragraph_format.line_spacing = 1.15
            b_run = p_body.add_run(stripped)
            b_run.font.name = 'Times New Roman'
            b_run.font.size = Pt(11)

    # Save document to memory buffer
    buffer = io.BytesIO()
    doc.save(buffer)
    buffer.seek(0)
    return buffer.getvalue()

class PDF(FPDF):
    def __init__(self, doc_type: str, logo_path: str = None):
        super().__init__()
        self.doc_type = doc_type
        self.logo_path = logo_path or (str(LOGO_PATH) if LOGO_PATH.exists() else None)

    def header(self):
        if self.logo_path and Path(self.logo_path).exists():
            try:
                self.image(self.logo_path, x=80, y=10, w=50)
                self.ln(25)
            except Exception:
                self.ln(10)
        else:
            self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(120, 120, 120)
        footer_text = f"{COMPANY_FOOTER}  |  Page {self.page_no()}/{{nb}}"
        self.cell(0, 10, footer_text, align='C')

def format_pdf(text: str, doc_type: str, logo_path: str = None) -> bytes:
    """Utilizes FPDF with custom header/footer, bold headings, and clean layout."""
    pdf = PDF(doc_type=doc_type, logo_path=logo_path)
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=20)

    # Document Title
    pdf.set_font('Helvetica', 'B', 16)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 10, doc_type.upper() if doc_type else "LEGAL DOCUMENT", align='C', new_x="LMARGIN", new_y="NEXT")
    pdf.ln(6)

    clean_txt = sanitize_text(text)
    lines = clean_txt.split('\n')

    for line in lines:
        stripped = line.strip()
        if not stripped:
            pdf.ln(3)
            continue

        if stripped.startswith('#'):
            heading_text = stripped.lstrip('#').strip()
            if heading_text.lower() == doc_type.lower():
                continue
            pdf.set_font('Helvetica', 'B', 12)
            pdf.set_text_color(30, 41, 59)
            pdf.multi_cell(0, 7, heading_text)
            pdf.ln(2)
        elif re.match(r'^(\d+\.|\b[A-Z\s]{4,}\b|Between:|WITNESSETH:|NOW, THEREFORE,)', stripped):
            pdf.set_font('Helvetica', 'B', 11)
            pdf.set_text_color(15, 23, 42)
            pdf.multi_cell(0, 6, stripped)
            pdf.ln(1)
        else:
            pdf.set_font('Helvetica', '', 10)
            pdf.set_text_color(51, 65, 85)
            pdf.multi_cell(0, 6, stripped)
            pdf.ln(1)

    return bytes(pdf.output())

def format_html_preview(text: str) -> str:
    """Converts output to stylized HTML blocks for inline display."""
    if not text:
        return ""
    clean_txt = sanitize_text(text)
    lines = clean_txt.split('\n')
    html_out = ["<div style='font-family: Inter, Roboto, sans-serif; color: #e2e8f0; background-color: #0f172a; padding: 25px; border-radius: 10px; border: 1px solid #334155;'>"]

    for line in lines:
        stripped = line.strip()
        if not stripped:
            html_out.append("<br/>")
            continue

        if stripped.startswith('#'):
            h_text = stripped.lstrip('#').strip()
            html_out.append(f"<h3 style='color: #60a5fa; margin-top: 15px; margin-bottom: 8px; border-bottom: 1px solid #334155; padding-bottom: 5px;'>{h_text}</h3>")
        elif re.match(r'^(\d+\.|\b[A-Z\s]{4,}\b|Between:|WITNESSETH:|NOW, THEREFORE,)', stripped):
            html_out.append(f"<p style='font-weight: 600; color: #f8fafc; margin-top: 10px; margin-bottom: 4px;'>{stripped}</p>")
        else:
            html_out.append(f"<p style='line-height: 1.6; color: #cbd5e1; margin-bottom: 8px;'>{stripped}</p>")

    html_out.append("</div>")
    return "\n".join(html_out)
