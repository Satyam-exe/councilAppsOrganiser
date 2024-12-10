import csv

from functions import details_from_id, regd_from_id, post_sec_from_id, name_from_id, post_prim_from_id
from header_codes import class_num

_applicant_email_ids = []
applicant_ids = []

with open('data/responses.csv', mode='r', encoding="utf8") as file:
    data_file = csv.reader(file)
    next(data_file)
    for row in data_file:
        _applicant_email_ids.append(row[1])

for email_id in _applicant_email_ids:
    class_of_applicant = details_from_id(email_id=email_id)[class_num]
    if class_of_applicant == 'VIII' or class_of_applicant == 'IX' or class_of_applicant == 'X' or class_of_applicant == 'XI':
        applicant_ids.append(email_id)

for email_id in applicant_ids:
    another_post = False if post_sec_from_id(email_id) == '[Not applied]' or post_sec_from_id(email_id) == '[Not permitted]' else True
    maximum_repetitions = 2 if another_post else 1

    admn_no = regd_from_id(email_id)

    with open('data/spreadsheet_high.csv', mode='r') as csv_file:
        spreadsheet_high = csv.reader(csv_file)
        next(spreadsheet_high)
        i=0
        j=0
        entries = []
        for row in spreadsheet_high:
            j+=1
            if admn_no == row[0]:
                i+=1
                entries.append(j)

        if post_prim_from_id(email_id) == post_sec_from_id(email_id):
            i+=1
        if i!=maximum_repetitions:
            print(f'{name_from_id(email_id)} has {i} entries while {maximum_repetitions} should be there.')





