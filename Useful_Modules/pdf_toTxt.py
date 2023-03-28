!pip install PyPDF2

def pdf_to_text(pdf_path, text_path):
    import PyPDF2
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        total_pages = len(pdf_reader.pages)
        extracted_text = ''

        for page_number in range(total_pages):
            pdf_page = pdf_reader.pages[page_number]
            extracted_text += pdf_page.extract_text()

    with open(text_path, 'w', encoding='utf-8') as text_file:
        text_file.write(extracted_text)

