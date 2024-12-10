import csv

from functions import details_from_id, post_prim_from_id, prev_positions_from_id, post_sec_from_id
from header_codes import class_num, regd_num, section_num, name_num


_applicant_ids = []
applicant_ids = []
with open('data/responses.csv', mode='r', encoding="utf8") as file:
    data_file = csv.reader(file)
    next(data_file)
    for row in data_file:
        _applicant_ids.append(row[1])



def create_high_school_spreadsheet():

    high_school_csv_file_path = 'data/spreadsheet_high.csv'

    data = [
        ['Reg. No.', 'Class', 'Name', 'Post', 'Entity', 'Previous Post']
    ]

    list_of_clubs = [
        'Eco Club',
        'Entrepreneurship Club',
        'Health and Wellness Club',
        'Heritage Club',
        'ICT Club',
        'Literary Club',
        'Maa Boli Club',
        'Maths Club',
        'Performing Arts Club',
        'Photography Club',
        'Quiz Club',
        'Science Club',
        'Self Advocacy Club',
        'Space and Robotics Club',
        'SPICMACAY Club',
        'TED-Ed Club',
        'Youth for Change Club',
        'Yuva Tourism Club',
    ]

    list_of_houses = [
        'Gulmohar House',
        'Jacaranda House',
        'Laburnum House',
        'Magnolia House'
    ]

    for email_id in _applicant_ids:
        class_of_applicant = details_from_id(email_id=email_id)[class_num]
        if class_of_applicant == 'VIII' or class_of_applicant == 'IX' or class_of_applicant == 'X' or class_of_applicant == 'XI':
            applicant_ids.append(email_id)

    def row_from_id(email_id, post, entity):
        details = details_from_id(email_id=email_id)
        return [details[regd_num], details[class_num] + '-' + details[section_num], details[name_num], post, entity,
                prev_positions_from_id(email_id)]

    def add_to_csv_high():
        with open(high_school_csv_file_path, mode='w', newline='', encoding='UTF-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(data)

    for email_id in applicant_ids:
        if post_prim_from_id(email_id) == 'President Student Council' or post_sec_from_id(email_id) == 'President Student Council':
            row = row_from_id(email_id, 'President', 'Student Council')
            data.append(row)

    for email_id in applicant_ids:
        if post_prim_from_id(email_id) == 'Vice President Student Council' or post_sec_from_id(email_id) == 'Vice President Student Council':
            row = row_from_id(email_id, 'Vice President', 'Student Council')
            data.append(row)

    for email_id in applicant_ids:
        if post_prim_from_id(email_id) == 'Secretary Student Council' or post_sec_from_id(email_id) == 'Secretary Student Council':
            row = row_from_id(email_id, 'Secretary', 'Student Council')
            data.append(row)

    for email_id in applicant_ids:
        if post_prim_from_id(email_id) == 'Editor-in-Chief (Digital Design Board)' or post_sec_from_id(email_id) == 'Editor-in-Chief (Digital Design Board)':
            row = row_from_id(email_id, 'Editor-in-Chief', 'Digital Design Board')
            data.append(row)

    for email_id in applicant_ids:
        if post_prim_from_id(email_id) == 'Editor (Digital Design Board)' or post_sec_from_id(email_id) == 'Editor (Digital Design Board)':
            row = row_from_id(email_id, 'Editor', 'Digital Design Board')
            data.append(row)

    for email_id in applicant_ids:
        if post_prim_from_id(email_id) == 'Editor-in-Chief (Editorial Board)' or post_sec_from_id(email_id) == 'Editor-in-Chief (Editorial Board)':
            row = row_from_id(email_id, 'Editor-in-Chief', 'Editorial Board')
            data.append(row)

    for email_id in applicant_ids:
        if post_prim_from_id(email_id) == 'Editor English (Editorial Board)' or post_sec_from_id(email_id) == 'Editor English (Editorial Board)':
            row = row_from_id(email_id, 'Editor English', 'Editorial Board')
            data.append(row)

    for email_id in applicant_ids:
        if post_prim_from_id(email_id) == 'Editor Hindi (Editorial Board)' or post_sec_from_id(email_id) == 'Editor Hindi (Editorial Board)':
            row = row_from_id(email_id, 'Editor Hindi', 'Editorial Board')
            data.append(row)

    for email_id in applicant_ids:
        if post_prim_from_id(email_id) == 'Editor Punjabi (Editorial Board)' or post_sec_from_id(email_id) == 'Editor Punjabi (Editorial Board)':
            row = row_from_id(email_id, 'Editor Punjabi', 'Editorial Board')
            data.append(row)

    for house in list_of_houses:
        temp_list1 = []
        temp_list2 = []
        for email_id in applicant_ids:
            prim_post = post_prim_from_id(email_id)
            sec_post = post_sec_from_id(email_id)
            house_name = house.replace(" House", "")
            if house_name in prim_post or house_name in sec_post:
                if prim_post == f"Captain  - {house_name}" or sec_post == f"Captain  - {house_name}":
                    temp_list1.append(email_id)
                if prim_post == f"Vice Captain  - {house_name}" or sec_post == f"Vice Captain  - {house_name}":
                    temp_list2.append(email_id)
        if temp_list1:
            temp_list1.sort()
            for _email_id in temp_list1:
                data.append(row_from_id(_email_id, 'Captain', house))
        if temp_list2:
            temp_list2.sort()
            for _email_id in temp_list2:
                data.append(row_from_id(_email_id, 'Vice Captain', house))

    for club in list_of_clubs:
        temp_list1 = []
        temp_list2 = []
        temp_list3 = []
        for email_id in applicant_ids:
            prim_post = post_prim_from_id(email_id)
            sec_post = post_sec_from_id(email_id)
            if club in prim_post or club in sec_post:
                if prim_post == f'President  - {club}' or sec_post == f'President  - {club}':
                    temp_list1.append(email_id)
                if prim_post == f'Vice President  - {club}' or sec_post == f'Vice President  - {club}':
                    temp_list2.append(email_id)
                if prim_post == f'Secretary  - {club}' or sec_post == f'Secretary  - {club}':
                    temp_list3.append(email_id)
        if temp_list1:
            temp_list1.sort()
            for _email_id in temp_list1:
                data.append(row_from_id(_email_id, 'President', club))
        if temp_list2:
            temp_list2.sort()
            for _email_id in temp_list2:
                data.append(row_from_id(_email_id, 'Vice President', club))
        if temp_list3:
            temp_list3.sort()
            for _email_id in temp_list3:
                data.append(row_from_id(_email_id, 'Secretary', club))

    for email_id in applicant_ids:
        if post_prim_from_id(email_id) == 'Class Representative' or post_sec_from_id(email_id) == 'Class Representative':
            if details_from_id(email_id)[class_num] == 'VIII':
                data.append(row_from_id(email_id, 'Class Representative', f"Class IX"))

    for email_id in applicant_ids:
        if post_prim_from_id(email_id) == 'Class Representative' or post_sec_from_id(email_id) == 'Class Representative':
            if details_from_id(email_id)[class_num] == 'IX':
                data.append(row_from_id(email_id, 'Class Representative', f"Class X"))

    for email_id in applicant_ids:
        if post_prim_from_id(email_id) == 'Class Representative' or post_sec_from_id(email_id) == 'Class Representative':
            if details_from_id(email_id)[class_num] == 'X':
                data.append(row_from_id(email_id, 'Class Representative', f"Class XI"))

    for email_id in applicant_ids:
        if post_prim_from_id(email_id) == 'Class Representative' or post_sec_from_id(email_id) == 'Class Representative':
            if details_from_id(email_id)[class_num] == 'XI':
                data.append(row_from_id(email_id, 'Class Representative', f"Class XII"))

    for email_id in applicant_ids:
        if post_prim_from_id(email_id) == 'Prefect' or post_sec_from_id(email_id) == 'Prefect':
            if details_from_id(email_id)[class_num] == 'VIII':
                data.append(row_from_id(email_id, 'Prefect', f"Class IX"))

    for email_id in applicant_ids:
        if post_prim_from_id(email_id) == 'Prefect' or post_sec_from_id(email_id) == 'Prefect':
            if details_from_id(email_id)[class_num] == 'IX':
                data.append(row_from_id(email_id, 'Prefect', f"Class X"))

    for email_id in applicant_ids:
        if post_prim_from_id(email_id) == 'Prefect' or post_sec_from_id(email_id) == 'Prefect':
            if details_from_id(email_id)[class_num] == 'X':
                data.append(row_from_id(email_id, 'Prefect', f"Class XI"))

    for email_id in applicant_ids:
        if post_prim_from_id(email_id) == 'Prefect' or post_sec_from_id(email_id) == 'Prefect':
            if details_from_id(email_id)[class_num] == 'XI':
                data.append(row_from_id(email_id, 'Prefect', f"Class XII"))


    add_to_csv_high()



def create_middle_school_spreadsheet():

    middle_school_csv_file_path = 'data/spreadsheet_middle.csv'

    data = [
        ['Reg. No.', 'Class', 'Name', 'Post', 'Previous Post']
    ]


    for email_id in _applicant_ids:
        class_of_applicant = details_from_id(email_id=email_id)[class_num]
        if class_of_applicant == 'V' or class_of_applicant == 'VI' or class_of_applicant == 'VII':
            applicant_ids.append(email_id)

    def row_from_id(email_id, post):
        details = details_from_id(email_id=email_id)
        return [details[regd_num], details[class_num] + '-' + details[section_num], details[name_num], post,
                prev_positions_from_id(email_id)]

    def add_to_csv_middle():
        with open(middle_school_csv_file_path, mode='w', newline='', encoding='UTF-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(data)

    for email_id in applicant_ids:
        if post_prim_from_id(email_id) == 'Class Representative' or post_sec_from_id(email_id) == 'Class Representative':
            if details_from_id(email_id)[class_num] == 'V':
                data.append(row_from_id(email_id, 'Class Representative'))

    for email_id in applicant_ids:
        if post_prim_from_id(email_id) == 'Class Representative' or post_sec_from_id(email_id) == 'Class Representative':
            if details_from_id(email_id)[class_num] == 'VI':
                data.append(row_from_id(email_id, 'Class Representative'))

    for email_id in applicant_ids:
        if post_prim_from_id(email_id) == 'Class Representative' or post_sec_from_id(email_id) == 'Class Representative':
            if details_from_id(email_id)[class_num] == 'VII':
                data.append(row_from_id(email_id, 'Class Representative'))
    for email_id in applicant_ids:
        if post_prim_from_id(email_id) == 'Student Council Member' or post_sec_from_id(email_id) == 'Student Council Member':
            if details_from_id(email_id)[class_num] == 'V':
                data.append(row_from_id(email_id, 'Student Council Member'))

    for email_id in applicant_ids:
        if post_prim_from_id(email_id) == 'Student Council Member' or post_sec_from_id(email_id) == 'Student Council Member':
            if details_from_id(email_id)[class_num] == 'VI':
                data.append(row_from_id(email_id, 'Student Council Member'))

    for email_id in applicant_ids:
        if post_prim_from_id(email_id) == 'Student Council Member' or post_sec_from_id(email_id) == 'Student Council Member':
            if details_from_id(email_id)[class_num] == 'VII':
                data.append(row_from_id(email_id, 'Student Council Member'))


    add_to_csv_middle()


if __name__ == '__main__':
    temp = int(input('Write 1 to create high school spreadsheet\nWrite 2 to create middle school spreadsheet\n'))
    match temp:
        case 1:
            create_high_school_spreadsheet()
        case 2:
            create_middle_school_spreadsheet()
        case _:
            print('Invalid input')