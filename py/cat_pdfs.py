import PyPDF2
import re
import sys


def extract_page_number(filename):
    match = re.search(r'_page_(\d+)', filename)
    return int(match.group(1)) if match else -1


def concat_pdfs(input_paths, output_path):
    pdf_writer = PyPDF2.PdfWriter()
    for path in input_paths:
        pdf_reader = PyPDF2.PdfReader(path)
        pdf_writer.add_page(pdf_reader.pages[0])

    with open(output_path, 'wb') as output_pdf_file:
        pdf_writer.write(output_pdf_file)


input_paths = sys.argv[2:]
output_path = sys.argv[1]
sorted_files = sorted(input_paths, key=extract_page_number)
concat_pdfs(sorted_files, output_path)
