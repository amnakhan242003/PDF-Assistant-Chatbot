
# PDF Chatbot Assistant

 A web-based PDF chatbot that allows users to upload PDF documents and ask questions. The chatbot extracts the most relevant sections from the uploaded PDFs using advanced NLP techniques and presents clear, well-formatted answers.




## Features

1. Upload PDF documents for analysis.
2. Extract relevant sections from PDFs using NLP embeddings.
3. Ask questions about the PDF and get contextually relevant  answers.
4. View the uploaded PDF directly in the browser.
5. Simple, user-friendly Streamlit interface.
6. Backend powered by Flask API with Python NLP models.



## Technologies used

Python 3

Flask (Backend API)

Streamlit (Frontend UI)

PyPDF2 (PDF extraction)

Sentence Transformers (all-MiniLM-L6-v2) for embeddings

Scikit-learn (Cosine similarity)

Docker & Docker Compose
##  Setup Instructions

1. Clone the Repository

```bash
git clone <repo url>
cd chatbot
```

2. Prerequisites
Docker & Docker Compose should be installed on machine and stable Internet connection for the first build (downloads large ML packages like PyTorch).

3. Build and Start Docker Containers
```bash
docker compose build   #Build the Docker images

docker compose up     #Start the containers

```
Backend Flask API will run on http://localhost:5000

Frontend Streamlit app will run on http://localhost:8501

4. Interact with the Chatbot
Open http://localhost:8501 in your browser.
## API Documentation
 ## Upload PDF

Endpoint: POST /upload_pdf

Description: Upload a PDF document to the chatbot. The text from the PDF will be processed and stored in the knowledge base.

| Parameter | Type | Description |
|-----------|------|-------------|
| file      | file | PDF file to upload |

## Ask a Question

Endpoint: POST /ask

Description: Submit a question, and the chatbot returns the most relevant section from the uploaded PDF.
| Parameter | Type | Description |
|-----------|------|-------------|
| question      | string | 	The question about the PDF |






## Author
- Amna Khan
- https://github.com/amnakhan242003

