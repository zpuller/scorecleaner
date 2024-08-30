import PyPDF2
import sys


def concat_pdfs(input_paths, output_path):
    pdf_writer = PyPDF2.PdfWriter()
    for path in input_paths:
        pdf_reader = PyPDF2.PdfReader(path)
        pdf_writer.add_page(pdf_reader.pages[0])

    with open(output_path, 'wb') as output_pdf_file:
        pdf_writer.write(output_pdf_file)


input_paths = sys.argv[2:]
output_path = sys.argv[1]
concat_pdfs(input_paths, output_path)
