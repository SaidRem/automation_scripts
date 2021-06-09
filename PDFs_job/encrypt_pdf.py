import os
import PyPDF2
from pathlib import Path

def encrypt_pdf(your_password):
    os.makedirs('encrypted_pdfs', exist_ok=True)

    for f in os.listdir():
        if f.endswith('.pdf'):
            with open(f, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfFileReader(pdf_file)
                if pdf_reader.isEncrypted:
                    continue
                pdf_writer = PyPDF2.PdfFileWriter()
                for page_num in range(pdf_reader.numPages):
                    pdf_writer.addPage(pdf_reader.getPage(page_num))
                pdf_writer.encrypt(your_password)
                with open(Path('encrypted_pdfs', f), 'wb') as encrypted_pdf:
                    pdf_writer.write(encrypted_pdf)
