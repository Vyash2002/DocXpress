import streamlit as st
from pdf2docx import Converter
import os
import tempfile

# Windows-specific for Word to PDF
try:
    import comtypes.client
    import pythoncom
    WINDOWS = True
except ImportError:
    WINDOWS = False

st.set_page_config(page_title="PDF ↔ Word Converter", layout="centered")
st.title("📄 PDF ↔ Word Converter")

st.markdown("Easily convert between PDF and Word (.docx) formats directly in your browser.")

option = st.radio("Choose Conversion Type:", ["PDF to Word", "Word to PDF"])
uploaded_file = st.file_uploader("Upload your file", type=["pdf", "docx"])

if uploaded_file and option == "PDF to Word":
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as input_pdf:
        input_pdf.write(uploaded_file.read())
        input_pdf_path = input_pdf.name

    output_path = input_pdf_path.replace(".pdf", ".docx")

    if st.button("Convert to Word (.docx)"):
        try:
            st.info("⏳ Converting PDF to Word...")
            cv = Converter(input_pdf_path)
            cv.convert(output_path, start=0, end=None)
            cv.close()

            with open(output_path, "rb") as f:
                st.success("✅ Conversion successful!")
                st.download_button("📥 Download Word File", data=f, file_name="converted.docx")

        except Exception as e:
            st.error(f"❌ Conversion failed: {e}")

elif uploaded_file and option == "Word to PDF":
    if not WINDOWS:
        st.warning("⚠️ Word to PDF works only on Windows with Microsoft Word installed.")
    else:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as input_docx:
            input_docx.write(uploaded_file.read())
            input_path = input_docx.name
            output_path = input_path.replace(".docx", ".pdf")

        if st.button("Convert to PDF"):
            try:
                st.info("⏳ Converting Word to PDF...")

                # COM initialization for thread safety
                pythoncom.CoInitialize()

                word = comtypes.client.CreateObject("Word.Application")
                word.Visible = False

                doc = word.Documents.Open(input_path)
                doc.SaveAs(output_path, FileFormat=17)  # 17 = wdFormatPDF
                doc.Close()
                word.Quit()

                pythoncom.CoUninitialize()

                with open(output_path, "rb") as f:
                    st.success("✅ Conversion successful!")
                    st.download_button("📥 Download PDF File", data=f, file_name="converted.pdf")

            except Exception as e:
                st.error(f"❌ Conversion failed: {e}")
