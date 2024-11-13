import os

import subprocess

from docx import Document
from docx.shared import Mm

from functions import *

TEMPLATE_PATH = './template/template.docx'
FINAL_PATH = './data/final/'


def create_docx(email_id):
    doc = Document(TEMPLATE_PATH)

    data = {
        'registration_number': regd_from_id(email_id),
        'email': email_id,
        'mobile_number': mobile_from_id(email_id),
        'name': name_from_id(email_id),
        'class_section': class_section_from_id(email_id),
        'previous_positions_held': prev_positions_from_id(email_id),
        'primary_post_applied': post_prim_from_id(email_id),
        'secondary_post_applied': post_sec_from_id(email_id),
        'answer_1': responses_from_id(email_id)[0],
        'answer_2': responses_from_id(email_id)[1],
        'answer_3': responses_from_id(email_id)[2],
    }
    image_path = f'./data/photos/{regd_from_id(email_id)}.jpg'
    for table in doc.tables:
        for row in table.rows:
            left_cell, right_cell = row.cells

            # Insert image if placeholder is found in the right cell
            if '{{ photograph }}' in right_cell.text:
                right_cell.text = ""
                if os.path.exists(image_path):
                    right_cell_paragraph = right_cell.paragraphs[0]
                    run = right_cell_paragraph.add_run()
                    run.add_picture(image_path, width=Mm(35), height=Mm(45))

            # Replace placeholders in the left cell text
            for placeholder, value in data.items():
                for paragraph in left_cell.paragraphs:
                    for run in paragraph.runs:
                        if f"{{{{ {placeholder} }}}}" in run.text:
                            # Split text around the placeholder and replace it with value
                            text_parts = run.text.split(f"{{{{ {placeholder} }}}}")
                            run.text = text_parts[0]  # Keep initial part of the run text
                            # Add new run for the placeholder replacement while copying formatting
                            new_run = paragraph.add_run(value)
                            new_run.bold = run.bold
                            new_run.italic = run.italic
                            new_run.font.size = run.font.size
                            # Add rest of text after placeholder
                            if len(text_parts) > 1:
                                end_run = paragraph.add_run(text_parts[1])
                                end_run.bold = run.bold
                                end_run.italic = run.italic
                                end_run.font.size = run.font.size

    # Replace placeholders in document paragraphs (outside the tables)
    for paragraph in doc.paragraphs:
        for placeholder, value in data.items():
            if f"{{{{ {placeholder} }}}}" in paragraph.text:
                for run in paragraph.runs:
                    if f"{{{{ {placeholder} }}}}" in run.text:
                        run.text = run.text.replace(f"{{{{ {placeholder} }}}}", value)

    # Save the document
    doc.save(f"{FINAL_PATH}/{regd_from_id(email_id)}.docx")


def convert_docx_to_pdf(email_id):
    docx_path = f"{FINAL_PATH}/{regd_from_id(email_id)}.docx"
    pdf_path = f"{FINAL_PATH}/{regd_from_id(email_id)}.pdf"

    subprocess.run(
        [r"C:\Program Files\LibreOffice\program\soffice.exe", "--headless", "--convert-to", "pdf", "--outdir",
         os.path.dirname(pdf_path), docx_path])

    if os.path.exists(pdf_path):
        os.remove(docx_path)