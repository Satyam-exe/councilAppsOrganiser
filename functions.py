import csv

from header_codes import *

def get_questions():
    with open('data/data.csv', mode='r', encoding='utf-8') as file:
        data_file = csv.reader(file)
        headers = next(data_file)
        return headers[32:]

def details_from_id(email_id):
    with open('data/data.csv', mode='r', encoding='utf-8') as file:
        data_file = csv.reader(file)
        for row in data_file:
            if row[email_id_num] == email_id:
                return row
            else:
                continue

def name_from_id(email_id):
    return details_from_id(email_id)[name_num]

def class_section_from_id(email_id):
    return details_from_id(email_id)[class_num] + '-' + details_from_id(email_id)[section_num]

def post_prim_from_id(email_id):
    details = details_from_id(email_id)
    applicant_class = details[class_num]
    match applicant_class:
        case 'V':
            post_applicant = details[post_v_num]
        case 'VI':
            post_applicant = details[post_vi_num]
        case 'VII':
            post_applicant = details[post_vii_num]
        case 'VIII':
            post_applicant = details[post_viii_num]
        case 'IX':
            post_applicant = details[post_ix_num]
        case 'X':
            post_applicant = details[post_x1_num]
        case 'XI':
            post_applicant = details[post_xi1_num]

    if 'Club' in post_applicant:
        post_applicant = post_applicant.replace('of a Club', '')
        match details[class_num]:
            case 'VIII':
                club = details[club_viii_num]
            case 'IX':
                club = details[club_ix_num]
            case 'X':
                club = details[club_x1_num]
            case 'XI':
                club = details[club_xi1_num]
        post_applicant = post_applicant + ' - ' + club

    if 'House' in post_applicant:
        post_applicant = post_applicant.replace('of a House', '')
        match details[class_num]:
            case 'X':
                house = details[house_x1_num]
            case 'XI':
                house = details[house_xi1_num]
        post_applicant = post_applicant + ' - ' + house

    return post_applicant


def post_sec_from_id(email_id):
    details = details_from_id(email_id)
    applicant_class = details[class_num]
    if applicant_class == 'X' or applicant_class == 'XI':
        match applicant_class:
            case 'X':
                if details[another_post_x_num] == 'No':
                    return "[Not applied]"
                post_applicant = details[post_x2_num]
            case 'XI':
                if details[another_post_xi_num] == 'No':
                    return "[Not applied]"
                post_applicant = details[post_xi2_num]
        if 'Club' in post_applicant:
            post_applicant = post_applicant.replace('of a Club', '')
            match details[class_num]:
                case 'VIII':
                    club = details[club_viii_num]
                case 'IX':
                    club = details[club_ix_num]
                case 'X':
                    club = details[club_x1_num]
                case 'XI':
                    club = details[club_xi1_num]
            post_applicant = post_applicant + ' - ' + club

        elif 'House' in post_applicant:
            post_applicant = post_applicant.replace('of a House', '')
            match details[class_num]:
                case 'X':
                    house = details[house_x1_num]
                case 'XI':
                    house = details[house_xi1_num]
            post_applicant = post_applicant + ' - ' + house

        return post_applicant
    else:
        return "[Not permitted]"

def responses_from_id(email_id):
    return details_from_id(email_id)[achievements_num:]

def mobile_from_id(email_id):
    return details_from_id(email_id)[mobile_num]

def regd_from_id(email_id):
    return details_from_id(email_id)[regd_num]

def prev_positions_from_id(email_id):
    details = details_from_id(email_id)
    if details[class_num] == 'V':
        return 'Not applicable'
    if details[class_num] == 'VI' or details[class_num] == 'VII' or details[class_num] == 'VIII':
        return 'Student Council Member' if details[held_prev_post_vi_vii_viii_num] == 'Yes' else 'No'
    if details[class_num] == 'IX' or details[class_num] == 'X' or details[class_num] == 'XI':
        return details[prev_posts_desc_num] if details[held_prev_post_ix_x_xi_num] == 'Yes' else 'No'