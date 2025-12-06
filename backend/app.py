
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from nlp_model import add_pdf_to_knowledge_base, answer_question

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return "Chatbot PDF Project API is running!"

@app.route("/upload_pdf", methods=["POST"])
def upload_pdf():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    pdf_file = request.files["file"]
    print("Uploading file:", pdf_file.filename)

    if pdf_file.filename == "":
        return jsonify({"error": "Invalid file"}), 400

    save_path = os.path.join(UPLOAD_FOLDER, pdf_file.filename)
    pdf_file.save(save_path)
    print("Saved PDF to:", save_path)

    try:
        add_pdf_to_knowledge_base(save_path)
        print("PDF added to knowledge base successfully!")
        return jsonify({"message": "PDF added to knowledge base", "file": pdf_file.filename})
    except Exception as e:
        print("Error adding PDF to KB:", str(e))
        return jsonify({"error": str(e)}), 500

@app.route("/ask", methods=["POST"])
def ask_question():
    data = request.get_json()
    question = data.get("question", "")

    if not question:
        return jsonify({"answer": "Please provide a question."})

    try:
        answer = answer_question(question)
        return jsonify({"answer": answer})
    except Exception as e:
        print("Error answering question:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True)
