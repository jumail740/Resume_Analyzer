import PyPDF2
import docx

def extract_text(file):
    if file.name.endswith('.pdf'):
        reader=PyPDF2.PdfReader(file)
        text=""
        for page in reader.pages:
            text+=page.extract_text() or ""
        return text
    elif file.name.endswith('.docx'):
        doc = docx.Document(file)
        return "\n".join([para.text for para in doc.paragraphs])

    return ""