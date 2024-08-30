import os
import sys

from PyPDF2 import PdfReader, PdfWriter


def split_pdf(input_pdf_path, output_folder):
    pdf_reader = PdfReader(input_pdf_path)

    for page_number in range(len(pdf_reader.pages)):
        pdf_writer = PdfWriter()
        pdf_writer.add_page(pdf_reader.pages[page_number])

        output_pdf_path = os.path.join(
            output_folder, f"page_{page_number + 1}.pdf")
        with open(output_pdf_path, "wb") as output_pdf:
            pdf_writer.write(output_pdf)


input_path, output_path = sys.argv[1:]

split_pdf(input_path, output_path)
