import streamlit as st
import requests

st.set_page_config(page_title="PDF Chatbot", page_icon="🤖", layout="centered")
st.title("📄 PDF Chatbot")

# ----------------------
# 1️⃣ Upload PDF
# ----------------------
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file is not None:
    files = {"file": uploaded_file.getvalue()}
    # Streamlit file_uploader returns a file object, so use .getvalue() for requests
    response = requests.post("http://127.0.0.1:5000/upload_pdf", files={"file": uploaded_file})
    if response.status_code == 200:
        st.success("PDF uploaded successfully!")
        text_preview = response.json().get("text_preview", "")
        st.subheader("PDF Text Preview:")
        st.write(text_preview)
    else:
        st.error("Failed to upload PDF!")

st.markdown("---")

# ----------------------
# 2️⃣ Ask a Question
# ----------------------
question = st.text_input("Ask a question about the PDF:")

if st.button("Get Answer"):
    if question.strip() == "":
        st.warning("Please type a question.")
    else:
        response = requests.post("http://127.0.0.1:5000/ask", json={"question": question})
        if response.status_code == 200:
            answer = response.json().get("answer", "")
            st.subheader("Answer:")
            st.write(answer)
        else:
            st.error("Failed to get answer from chatbot!")
