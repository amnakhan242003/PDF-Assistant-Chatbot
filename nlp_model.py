import re
import numpy as np
from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# ----------------------------
# Embedding model for section retrieval
# ----------------------------
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# ----------------------------
# Knowledge base
# ----------------------------
knowledge_base = {
    "sections": [],
    "embeddings": np.array([])
}

# ----------------------------
# PDF extraction
# ----------------------------
def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text.strip()

# ----------------------------
# Split text into sections
# ----------------------------
def split_into_sections(text):
    sections = re.split(r'\n(?=\d+(\.\d+)*\s)', text)
    return [section.strip() for section in sections if section.strip()]

# ----------------------------
# Add PDF to KB
# ----------------------------
def add_pdf_to_knowledge_base(file_path):
    text = extract_text_from_pdf(file_path)
    sections = split_into_sections(text)
    embeddings = embedding_model.encode(sections)

    knowledge_base["sections"].extend(sections)
    if knowledge_base["embeddings"].size == 0:
        knowledge_base["embeddings"] = embeddings
    else:
        knowledge_base["embeddings"] = np.vstack([knowledge_base["embeddings"], embeddings])

# ----------------------------
# Retrieve most relevant section
# ----------------------------
def answer_question(question):
    if not knowledge_base["sections"]:
        return "Knowledge base is empty. Upload a PDF first."

    q_emb = embedding_model.encode([question])
    sims = cosine_similarity(q_emb, knowledge_base["embeddings"])
    top_idx = sims[0].argmax()
    relevant_section = knowledge_base["sections"][top_idx]

    # Format the relevant section nicely
    response = f"### 📄 Relevant Section from Document:\n{relevant_section}"
    return response
