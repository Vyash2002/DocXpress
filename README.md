📄 DocXpress – PDF ↔ Word Converter
DocXpress is a sleek and efficient Streamlit-based web application that enables seamless conversion between PDF and Word (.docx) formats. Whether you're looking to extract editable content from a PDF or convert a Word file into a polished PDF, DocXpress has you covered—all from your browser.

✨ Features
🔁 Two-way Conversion: Convert PDF to Word and Word to PDF

📂 Drag-and-Drop Upload: Simple and intuitive file uploads

💻 Lightweight UI: Built using Streamlit for a fast and clean experience

🧠 Smart Conversion: Uses pdf2docx and docx2pdf/comtypes under the hood

✅ No Ads, No Limits: 100% local and private

🛠️ Tech Stack
Feature	Library Used	Platform Support
PDF → Word	pdf2docx	✅ Cross-platform
Word → PDF	docx2pdf, comtypes, pywin32	⚠️ Windows Only (MS Word Required)

🚀 Getting Started
1. Clone the Repository
git clone https://github.com/yourusername/docxpress.git
cd docxpress
2. Install Dependencies
pip install -r requirements.txt

▶️ Run the App
streamlit run DocXpress.py
Open http://localhost:8501 in your browser to use the app.

📁 Project Structure
docxpress/
├── pdf_word_converter.py   # Main Streamlit app
├── requirements.txt        # Dependencies
└── README.md               # Project documentation
⚠️ Notes
Word to PDF conversion only works on Windows, and requires Microsoft Word installed.

Conversion speed depends on file size and system performance.

🧠 Future Enhancements
🔄 Batch file upload and conversion

🔒 PDF password protection

🖋️ Editable preview before download

🌐 Deploy to Streamlit Cloud or Hugging Face Spaces
