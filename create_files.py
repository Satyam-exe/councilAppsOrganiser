import csv

from functions import details_from_id
from header_codes import class_num
from template import create_docx, convert_docx_to_pdf


def generate_application(email_id):
    create_docx(email_id)
    convert_docx_to_pdf(email_id)


if __name__ == '__main__':
    applicant_ids = []
    with open('data/responses.csv', mode='r', encoding="utf8") as file:
        data_file = csv.reader(file)
        next(data_file)
        for row in data_file:
            applicant_ids.append(row[1])
    i=0
    for email_id in applicant_ids:
        if details_from_id(email_id)[class_num] == "VIII" or details_from_id(email_id)[class_num] == "IX" or details_from_id(email_id)[class_num] == "X" or details_from_id(email_id)[class_num] == "XI":
            generate_application(email_id)
