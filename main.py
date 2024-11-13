import csv

from template import create_docx, convert_docx_to_pdf


def generate_application(email_id):
    create_docx(email_id)
    convert_docx_to_pdf(email_id)


if __name__ == '__main__':
    applicant_ids = []
    with open('data/data.csv', mode='r', encoding="utf8") as file:
        data_file = csv.reader(file)
        next(data_file)
        for row in data_file:
            applicant_ids.append(row[1])
    for email_id in applicant_ids:
        generate_application(email_id)
