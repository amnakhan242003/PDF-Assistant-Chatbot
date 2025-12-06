import streamlit as st
import requests
import base64

st.set_page_config(page_title="PDF Chatbot", page_icon="📄", layout="wide")

st.markdown("""
<style>
.pdf-viewer {
    border: 2px solid #ddd;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

st.title("🤖 PDF Chatbot Assistant")

uploaded_file = st.file_uploader("📤 Upload PDF", type=["pdf"])

pdf_bytes = None
if uploaded_file:
    pdf_bytes = uploaded_file.getvalue()

    
    response = requests.post(
        "http://127.0.0.1:5000/upload_pdf",
        files={"file": uploaded_file}
    )

    if response.status_code == 200:
        st.success("PDF uploaded successfully!")

        st.markdown("---")

        st.subheader("📚 View PDF")

        base64_pdf = base64.b64encode(pdf_bytes).decode("utf-8")
        pdf_display = f"""
            <iframe src="data:application/pdf;base64,{base64_pdf}" 
            width="100%" height="500px" class="pdf-viewer"></iframe>
        """
        st.markdown(pdf_display, unsafe_allow_html=True)
    else:
        st.error("Error uploading PDF")

st.markdown("---")

st.subheader("💬 Ask a Question")

question = st.text_input("Ask a question about the PDF:")

if st.button("Get Answer"):
    if not uploaded_file:
        st.warning("Please upload a PDF first.")
    elif question.strip() == "":
        st.warning("Please type a question.")
    else:
        try:
            response = requests.post(
                "http://127.0.0.1:5000/ask",
                json={"question": question}
            )

            if response.status_code == 200:
                answer = response.json().get("answer", "")

                if answer:
                    st.markdown(answer, unsafe_allow_html=True)   
                else:
                    st.info("No relevant section found.")
            else:
                st.error("Error fetching answer.")
        except Exception as e:
            st.error(f"Error: {str(e)}")
