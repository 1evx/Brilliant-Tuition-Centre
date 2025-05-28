# The following code done by Lew Wai How
from datetime import datetime
from random import randint
import hashlib


# -----------------------------------------------common function--------------------------------------------------------
def read_all(file_name):
    # Read all row which in the file given and store to list
    # Return the list
    read_list = []
    with open(file_name, mode="r") as read_file:
        for read_line in read_file:
            read_line_str = read_line.replace("\n", "")
            read_line_list = read_line_str.split(",")
            read_list.append(read_line_list)
    return read_list


def find_one(file_name, start_reference_column, end_reference_column, reference_item):
    # Read one row that match the reference which in the file given
    for read_line in read_all(file_name):
        find_line = read_line[start_reference_column: end_reference_column]
        find_line_str = ",".join(find_line)
        if find_line_str == reference_item:
            return read_line


def find_more(file_name, start_reference_column, end_reference_column, reference_item):
    # Retrieve some row that match the reference from the particular file
    find_list = []
    for read_line in read_all(file_name):
        find_line = read_line[start_reference_column: end_reference_column]
        find_line_str = ",".join(find_line)
        if find_line_str == reference_item:
            find_list.append(read_line)
    return find_list


def edit(file_name, start_reference_column, end_reference_column, reference, edit_column, edit_item):
    # Find the row that match the reference from the particular file
    edit_str = ""
    for read_line in read_all(file_name):
        find_line = read_line[start_reference_column: end_reference_column]
        find_line_str = ",".join(find_line)
        if find_line_str == reference:
            # Update one information in the row
            read_line[edit_column] = edit_item
        read_line_str = ",".join(read_line)
        edit_str += read_line_str + "\n"
    with open(file_name, mode="w") as change_file:
        change_file.write(edit_str)


def delete(file_name, delete_row):
    # Delete a row in the txt file
    with open(file_name, "r") as old_file:
        with open(file_name, "r+") as new_file:
            start_row = 0
            while start_row < delete_row:
                old_file.readline()
                start_row += 1
            current_point = old_file.tell()
            new_file.seek(current_point, 0)
            old_file.readline()
            next_row = old_file.readline()
            while next_row:
                new_file.write(next_row)
                next_row = old_file.readline()
            new_file.truncate()


def register(file_name, register_list):
    # Add a row with information to the txt file
    register_item = ",".join(register_list) + "\n"
    with open(file_name, mode="a") as register_file:
        register_file.write(register_item)


def retrieve_level_or_subject(levels_or_subjects, level):
    # Retrieve all level or Retrieve subjects which belong to the level given
    level_and_subject = {"FORM1": ["BAHASA MALAYSIA", "ENGLISH", "MATHS", "SCIENCE", "SEJARAH"],
                         "FORM2": ["BAHASA MALAYSIA", "ENGLISH", "MATHS", "SCIENCE", "SEJARAH"],
                         "FORM3": ["BAHASA MALAYSIA", "ENGLISH", "MATHS", "SCIENCE", "SEJARAH"],
                         "FORM4": ["BAHASA MALAYSIA", "ENGLISH", "MATHS", "SCIENCE", "SEJARAH", "ADD MATHS", "PHYSICS",
                                   "CHEMISTRY", "BIOLOGY"],
                         "FORM5": ["BAHASA MALAYSIA", "ENGLISH", "MATHS", "SCIENCE", "SEJARAH", "ADD MATHS", "PHYSICS",
                                   "CHEMISTRY", "BIOLOGY"]
                         }
    if levels_or_subjects == "levels":
        levels = level_and_subject.keys()
        levels_list = list(levels)
        return levels_list
    else:
        subjects_in_level = level_and_subject.get(level)
        return subjects_in_level


def retrieve_subjects_fee(subject_name):
    # Retrieve subject fee which belong to the subject given
    subjects_fee = {"BAHASA MALAYSIA": 30,
                    "ENGLISH": 30,
                    "MATHS": 45,
                    "SCIENCE": 45,
                    "SEJARAH": 30,
                    "ADD MATHS": 50,
                    "ACCOUNTING": 45,
                    "ECONOMIC": 45,
                    "PHYSICS": 50,
                    "CHEMISTRY": 50,
                    "BIOLOGY": 50,
                    "NULL": 0
                    }
    subject_fee = subjects_fee.get(subject_name)
    return subject_fee


def view_levels_and_subjects():
    # Display all level and subject
    levels_list = retrieve_level_or_subject("levels", None)
    for level in levels_list:
        subjects_list = retrieve_level_or_subject("subjects", level)
        subjects = " / ".join(subjects_list)
        print(f"{level}: {subjects}\n")


def return_home_page(continue_statement):
    # Give user a chance to return to home page
    while True:
        back_choice = input(f"Enter 1 to return to home page / Enter 0 to {continue_statement}: ")
        if back_choice == "1":
            print("\nReturn to home page\n")
            return True
        elif back_choice == "0":
            return False
        else:
            print("Invalid command!!!\nPlease enter right command")


def get_and_verify_month():
    # Ask user to enter month and identify the validation of input
    while True:
        month = input("Please enter Month of the payment pay for (exp: January): ").capitalize().strip()
        try:
            datetime.strptime(month, "%B")
            return month
        except ValueError:
            print("Invalid month")
            if return_home_page("re-enter the month"):
                return


def get_and_verify_year():
    # Ask user to enter year and identify the validation of input
    while True:
        year = input("Please enter Year of the payment pay for (exp: 2023): ").strip()
        try:
            datetime.strptime(year, "%Y")
            return year
        except ValueError:
            print("Invalid Year")
            if return_home_page("re-enter the year"):
                return


def get_and_verify_class_date():
    # Ask user to enter date and identify the validation of input
    while True:
        class_date = input("Please enter Class Date (exp: 1 August 2023): ")
        try:
            datetime.strptime(class_date, "%d %B %Y")
            return class_date
        except ValueError:
            print("Invalid date")
            if return_home_page("re-enter class date"):
                return


def get_and_verify_class_venue():
    # Ask user to enter venue and identify the validation of input
    while True:
        class_venue = input("Please enter Class Venue (exp: A-01): ").upper()
        if class_venue[0].isalpha() and class_venue[1] == "-" and class_venue[2:].isdigit():
            return class_venue
        else:
            print("Invalid Venue")
            if return_home_page("re-enter class venue"):
                return


def get_and_verify_class_time(start_or_end):
    # Ask user to enter time and identify the validation of input
    while True:
        class_time = input(f"Please enter Class {start_or_end} Time (exp: 10.00 AM): ")
        try:
            datetime.strptime(class_time, "%I.%M %p")
            return class_time
        except ValueError:
            print("Invalid Time")
            if return_home_page(f"re-enter Class {start_or_end} Time"):
                return


def crypt_password(user_password):
    # Encrypt password by using hash algorithm
    sha256 = hashlib.sha256()
    sha256.update(user_password.encode("utf-8"))
    user_password_sha256 = sha256.hexdigest()
    return user_password_sha256


def generate_user_id_and_password(role_name):
    # Auto generate the role's ID and password
    if role_name == "stud":
        check_file = "payment.txt"
    else:
        check_file = role_name + ".txt"
    all_user_id = []
    for user_info in read_all(check_file):
        all_user_id.append(user_info[0])
    while True:
        code = str(randint(1, 9999))
        id_code = "0" * (4 - len(code)) + code
        user_id = role_name + id_code
        if user_id not in all_user_id:
            user_password = user_id + f"@B{id_code}"
            user_password_crypt = crypt_password(user_password)
            return [user_id, user_password_crypt]


def get_and_verify_role_level_for_registration(prompt_statement):
    # Ask user to enter the level of student or the assign level of tutor and identify the validation of input
    while True:
        role_level = input(f"Enter {prompt_statement} to register the account (exp: FORM1): ").upper().strip()
        levels_list = retrieve_level_or_subject("levels", None)
        if role_level in levels_list:
            return role_level
        else:
            print("\nInvalid level")
            if return_home_page(f"re-enter the {prompt_statement}"):
                return


def get_and_verify_stud_id_in_payment_file(prompt_statement):
    # Ask user to enter the student's ID and identify the validation of id by matching with payment file
    while True:
        stud_id = input(f"Please enter student id to {prompt_statement}: ").strip()
        stud_info_id = find_one("stud.txt", 0, 1, stud_id)
        if stud_info_id:
            return stud_id
        else:
            print("Invalid Student ID")
            if return_home_page("re-enter the student id"):
                return


def change_password(user_file, user_id):
    # Allow user to change own password
    # user must key in original password, new password and confirm password
    # the length of new password must between 8 and 16
    print("\nHome Page >>> Change Password")
    print("-" * 30 + "Change Password" + "-" * 30)
    while True:
        current_password = find_one(user_file, 0, 1, user_id)[1]
        ori_password = input("original password: ").strip()
        ori_password_crypt = crypt_password(ori_password)
        if ori_password_crypt == current_password:
            new_password = input("New password: ").strip()
            confirm_password = input("Confirm password: ").strip()
            if new_password == confirm_password:
                if 8 <= len(new_password) <= 16:
                    new_password_crypt = crypt_password(new_password)
                    edit(user_file, 0, 1, user_id, 1, new_password_crypt)
                    print("-" * 30 + "\nChange password success\n" + "-" * 30 + "\nReturn to home page\n")
                    return
                else:
                    print("Length of your password must minimum 8 and maximum 16")
            else:
                print("New password and Confirm password does not match")
        else:
            print("Wrong original password")
        if return_home_page("re-enter the password"):
            return


def update_profile(user_file, user_id):
    # Allow user to update own profile
    # the profile can be modifiable are address, email and contact number
    print("\nHome Page >>> Update Profile")
    print("-" * 30 + "Update Profile" + "-" * 30)
    user = find_one(user_file, 0, 1, user_id)
    print(
        f"Name: {user[2]}\nIC or Passport: {user[3]}\nAddress: {user[4]}\nEmail: {user[5]}\nContact Number: {user[6]}\n")
    update_data = ["Address", "Email", "Contact Number"]
    if return_home_page("update own profile"):
        print("\nReturn to home page\n")
        return
    for index, data in enumerate(update_data):
        print(f"\nEnter {index + 1}: Update {data}")
    while True:
        value = input("\nEnter a number to update the user data: ")
        try:
            value = int(value)
            if 0 < value <= len(update_data):
                break
            else:
                print("Invalid number")
                if return_home_page("re-enter the number"):
                    return
        except ValueError:
            print("Invalid user data number")
            if return_home_page("re-enter the number"):
                return
    if value == 1:
        update_item = input("Enter new address: ")
    elif value == 2:
        update_item = input("Enter new email: ")
    else:
        update_item = input("Enter new contact number: ")
    edit(user_file, 0, 1, user_id, value + 3, update_item)
    print("-" * 30 + "\nUpdate profile success\n" + "-" * 30 + "\nReturn to home page\n")


# ---------------------------------------------End common function-----------------------------------------------------

# ----------------------------------------------Admin functionality----------------------------------------------------
def admin_ui(user_id):
    # Direct admin to this function when login success
    # Display all functionality to admin
    # Ask admin to choose function
    admin_functions = ["Register Receptionist", "Register Tutor", "View and Delete Receptionist",
                       "View and Delete Tutor", "View monthly income report", "Change Password", "Update Profile",
                       "Log out"]
    while True:
        print("-" * 30 + "Admin Home Page" + "-" * 30)
        for index, function in enumerate(admin_functions):
            print(f"Enter {index + 1}: {function}")
        choice = input("Enter number: ")
        if choice == "1":
            register_recep()
        elif choice == "2":
            register_tutor()
        elif choice == "3":
            delete_recep()
        elif choice == "4":
            delete_tutor()
        elif choice == "5":
            view_income()
        elif choice == "6":
            change_password("admin.txt", user_id)
        elif choice == "7":
            update_profile("admin.txt", user_id)
        elif choice == "8":
            print("Log out success\n")
            return "out"
        else:
            print("Invalid command")


def register_recep():
    # Register Receptionist by entering name, ic, address, contact and email
    # Not allow empty input
    # ID and password generated automatically
    print("\nHome Page >>> Register Receptionist")
    print("-" * 30 + f"Register Receptionist" + "-" * 30)
    recep_info_list = ["Receptionist's Name",
                       "Receptionist's IC or Passport",
                       "Receptionist's Address",
                       "Receptionist's Contact Number",
                       "Receptionist's Email"]
    new_recep_info = []
    id_and_password = generate_user_id_and_password("recep")
    recep_id = id_and_password[0]
    print(f"Receptionist's ID generated: {recep_id}")
    recep_password = id_and_password[1]
    new_recep_info.append(recep_id)
    new_recep_info.append(recep_password)
    for recep_data in recep_info_list:
        while True:
            data = input(f"Please enter {recep_data} to register Receptionist account: ").strip()
            if data != "":
                break
            else:
                print("You must enter something !!!")
                if return_home_page(f"re-enter {recep_data}"):
                    return
        new_recep_info.append(data)
    register("recep.txt", new_recep_info)
    print("-" * 30 + "\nRegister Receptionist success\n" + "-" * 30 + "\nReturn to home page\n")


def register_tutor():
    # Register Tutor by entering name, ic, address, contact, email and assign level and subject
    # Not allow empty input and invalid level and subject
    # ID and password generated automatically
    # Display all valid level and subject before registering
    print("\nHome Page >>> Register Tutor")
    print("-" * 30 + f"Register Tutor" + "-" * 30)
    tutor_info_list = ["Tutor's Name",
                       "Tutor's IC or Passport",
                       "Tutor's Address",
                       "Tutor's Contact Number",
                       "Tutor's Email"]
    print("(Levels and Subjects)")
    view_levels_and_subjects()
    new_tutor_info = []
    id_and_password = generate_user_id_and_password("tutor")
    tutor_id = id_and_password[0]
    print(f"Tutor's ID generated: {tutor_id}")
    tutor_password = id_and_password[1]
    new_tutor_info.append(tutor_id)
    new_tutor_info.append(tutor_password)
    for tutor_data in tutor_info_list:
        while True:
            data = input(f"Please enter {tutor_data} to register Tutor account: ").strip()
            if data != "":
                break
            else:
                print("You must write something !!!")
                if return_home_page(f"re-enter {tutor_data}"):
                    return None
        new_tutor_info.append(data)
    tutor_assign_level = get_and_verify_role_level_for_registration("Tutor's in-charge level")
    if not tutor_assign_level:
        return
    else:
        new_tutor_info.append(tutor_assign_level)
    while True:
        tutor_assign_subject = input(f"Enter Tutor's in-charge subject to register the account: ").upper().strip()
        subject_info = retrieve_level_or_subject("subjects", tutor_assign_level)
        if tutor_assign_subject in subject_info:
            new_tutor_info.append(tutor_assign_subject)
            break
        else:
            print("\nInvalid Subject")
            if return_home_page(f"re-enter the Tutor's in-charge subject"):
                return
    register("tutor.txt", new_tutor_info)
    print("-" * 30 + "\nRegister Tutor Success\n" + "-" * 30 + "\nReturn to home page\n")


def delete_recep():
    # Display all receptionist account's information before deleting
    # Ask admin to enter receptionist's id to delete account
    # Not allow to enter receptionist's id which does not exist
    print("\nHome Page >>> Delete Receptionist")
    print("-" * 30 + "Delete Receptionist" + "-" * 30)
    recep_list = read_all("recep.txt")
    if not recep_list:
        print("No Receptionist Information")
        return
    recep_list.sort(key=lambda id: (id[0], "recep"))
    for recep_info in recep_list:
        print(f"Receptionist ID: {recep_info[0]}\nReceptionist Name: {recep_info[2]}\n"
              f"Receptionist IC or Passport: {recep_info[3]}\nReceptionist Address: {recep_info[4]}\n"
              f"Receptionist Contact Number: {recep_info[5]}\nReceptionist Email: {recep_info[6]}\n"
              + "~" * 70)
    if return_home_page("delete receptionist's information"):
        return
    while True:
        delete_recep_id = input(f"Please enter Receptionist's ID to delete the account: ")
        delete_recep_info = find_one("recep.txt", 0, 1, delete_recep_id)
        if delete_recep_info:
            recep_delete_row = recep_list.index(delete_recep_info)
            break
        else:
            print("\nReceptionist ID does not exist")
            if return_home_page("re-enter the receptionist's id"):
                return
    delete("recep.txt", recep_delete_row)
    print("-" * 30 + "\nDelete Receptionist Success\n" + "-" * 30 + "\nReturn to home page\n")


def delete_tutor():
    # Display all tutor account's information before deleting
    # Ask admin to enter tutor's id to delete account
    # Not allow to enter tutor's id which does not exist
    print(f"\nHome Page >>> Delete Tutor")
    print("-" * 30 + f"Delete Receptionist" + "-" * 30)
    tutor_list = read_all("tutor.txt")
    if not tutor_list:
        print("No Tutor Information")
        return
    tutor_list.sort(key=lambda id: (id[0], "tutor"))
    # Allow admin to view all tutor information before deleting account
    for tutor_info in tutor_list:
        print(f"Tutor's ID: {tutor_info[0]}\nTutor's Name: {tutor_info[2]}\n"
              f"Tutor's IC or Passport: {tutor_info[3]}\nTutor's Address: {tutor_info[4]}\n"
              f"Tutor's Contact Number: {tutor_info[5]}\nTutor's Email: {tutor_info[6]}\n"
              f"Tutor's Assign Level: {tutor_info[7]}\nTutor's Assign Subject: {tutor_info[8]}\n"
              + "~" * 70)
    if return_home_page("delete tutor's information"):
        return
    # Get tutor id and identify the validation of the tutor id for deleting account
    while True:
        delete_tutor_id = input(f"Please enter Tutor ID to delete the account: ").strip()
        delete_tutor_info = find_one("tutor.txt", 0, 1, delete_tutor_id)
        if delete_tutor_info:
            tutor_delete_row = tutor_list.index(delete_tutor_info)
            break
        else:
            print("\nTutor's ID does not exist")
            if return_home_page("re-enter the tutor's id"):
                return
    delete("tutor.txt", tutor_delete_row)
    print("-" * 30 + "\nDelete Tutor Success\n" + "-" * 30 + "\nReturn to home page\n")


def view_income():
    # Ask admin to enter month and year to view the monthly income report
    # The report will show by level and subject
    print("\nHome Page >>> View Student Monthly Income")
    print("-" * 30 + "View Monthly Income" + "-" * 30)
    month = get_and_verify_month()
    year = get_and_verify_year()
    if not month or not year:
        return
    date = f"{month} {year}"
    payment_list_date = find_more("payment.txt", 1, 2, date)
    payment_list_status = find_more("payment.txt", 10, 11, "PAID")
    payment_list_date_level_status = []
    if not payment_list_status or not payment_list_date:
        print("No available of income in this month\nReturn to home page\n")
        return
    else:
        for payment_info_status in payment_list_status:
            if payment_info_status in payment_list_date:
                payment_list_date_level_status.append(payment_info_status)
    print(f"\nDate: {date}\n")
    total_fee = 0
    for level in retrieve_level_or_subject("levels", None):
        total_level_fee = 0
        print(f"Level: {level}")
        subject_info = retrieve_level_or_subject("subjects", level)
        for subject_num, subject in enumerate(subject_info):
            total_subject_fee = 0
            for subject_enrolled_num in range(1, 4):
                payment_list_subject_enrolled = find_more("payment.txt", 3 + subject_enrolled_num,
                                                          4 + subject_enrolled_num, subject)
                if payment_list_subject_enrolled:
                    payment_list_level = find_more("payment.txt", 2, 3, level)
                    for payment_info_subject_enrolled in payment_list_subject_enrolled:
                        if payment_info_subject_enrolled in payment_list_date_level_status and payment_info_subject_enrolled in payment_list_level:
                            subject_fee = payment_info_subject_enrolled[subject_enrolled_num + 6]
                            total_subject_fee += int(subject_fee)
            print(f"\tSubject{subject_num + 1}: {subject}\n\tTotal income: RM{total_subject_fee}\n")
            total_level_fee += total_subject_fee
        total_fee += total_level_fee
        print(f"Total income of {level}: {total_level_fee}\n")
    print("-" * 30 + f"\nTotal income of {month} {year} is RM {total_fee}\n" + "-" * 30 + "\nReturn to home page\n")


# ---------------------------------------------End Admin functionality--------------------------------------------------

# The following code done by Tan Po Yeh
# --------------------------------------------Receptionist functionality------------------------------------------------
def recep_ui(user_id):
    # Direct receptionist to this function when login success
    # Display all functionality to receptionist
    # Ask receptionist to choose function
    recep_functions = ["Register and Enroll Students", "View Student's Request and Update student subject enrollment",
                       "Generate Student Payment", "Accept payment", "Generate receipt", "View and Delete Student",
                       "Add News", "Delete News", "Change Password", "Update Profile", "Log out"]
    while True:
        print("-" * 30 + "Receptionist Home Page" + "-" * 30)
        for index, function in enumerate(recep_functions):
            print(f"Enter {index + 1}: {function}")
        choice = input("Enter number: ")
        if choice == "1":
            register_stud()
        elif choice == "2":
            update_stud()
        elif choice == "3":
            generate_stud_payment()
        elif choice == "4":
            accept_payment(user_id)
        elif choice == "5":
            generate_receipt()
        elif choice == "6":
            delete_stud()
        elif choice == "7":
            add_news()
        elif choice == "8":
            delete_news()
        elif choice == "9":
            change_password("recep.txt", user_id)
        elif choice == "10":
            update_profile("recep.txt", user_id)
        elif choice == "11":
            print("Log out success\n")
            return "out"
        else:
            print("Invalid command")


def register_stud():
    # Register student by entering name, ic, address, contact, email and level enrolled and subject enrolled
    # Not allow empty input and invalid level and subject
    # ID and password generated automatically
    # Display all valid level and subject before registering
    print("\nHome Page >>> Register Students")
    print("-" * 30 + "Register Students" + "-" * 30)
    stud_info_list = ["Student's Name",
                      "Student's IC or Passport",
                      "Student's Address",
                      "Student's Contact Number",
                      "Student's Email"]
    view_levels_and_subjects()
    new_stud_info = []
    id_and_password = generate_user_id_and_password("stud")
    stud_id = id_and_password[0]
    print(f"Student's ID generated: {stud_id}")
    stud_password = id_and_password[1]
    new_stud_info.append(stud_id)
    new_stud_info.append(stud_password)
    for stud_data in stud_info_list:
        while True:
            data = input(f"Please enter {stud_data} to register Student account: ").strip()
            if data != "":
                break
            else:
                print("You must enter something !!!")
                if return_home_page(f"re-enter {stud_data}"):
                    return
        new_stud_info.append(data)
    month_of_enrollment = datetime.now().strftime("%d %B %Y")
    new_stud_info.append(month_of_enrollment)
    stud_level = get_and_verify_role_level_for_registration("Student's level")
    if not stud_level:
        return
    else:
        new_stud_info.append(stud_level)
    for stud_subject_num in range(1, 4):
        while True:
            student_subject = input(
                f"Enter Student Subject {stud_subject_num} to register the account (Enter NULL if no subject enroll): ").upper().strip()
            subject_info = retrieve_level_or_subject("subjects", stud_level)
            if student_subject in subject_info or student_subject == "NULL":
                new_stud_info.append(student_subject)
                break
            else:
                print("\nInvalid Subject")
                if return_home_page(f"re-enter the Subject {stud_subject_num}"):
                    return
    register("stud.txt", new_stud_info)
    generate_payment_after_register(stud_id)
    print("-" * 30 + "\nRegister Student Success\nAdd Student Education fee list of this month Success\n" + "-" * 30 +
          "\nReturn to home page\n")


def generate_payment_after_register(stud_id):
    # Direct to this page when registering student success
    # Student's education fee bill generated automatically for registration month
    stud_info_id = find_one("stud.txt", 0, 1, stud_id)
    date_of_education_fee = datetime.now().strftime("%B %Y")
    date_of_payment_done = "NULL"
    level = stud_info_id[8]
    subject1 = stud_info_id[9]
    subject2 = stud_info_id[10]
    subject3 = stud_info_id[11]
    subject1_fee = str(retrieve_subjects_fee(subject1))
    subject2_fee = str(retrieve_subjects_fee(subject2))
    subject3_fee = str(retrieve_subjects_fee(subject3))
    payment_status = "UNPAID"
    accept_payment_by = "NULL"
    new_payment_info = [stud_id, date_of_education_fee, level, date_of_payment_done, subject1, subject2,
                        subject3, subject1_fee, subject2_fee, subject3_fee, payment_status, accept_payment_by]
    register("payment.txt", new_payment_info)


def view_stud_request():
    # Display all request no.
    stud_request_list_pending = find_more("request.txt", 5, None, "STILL PENDING")
    if not stud_request_list_pending:
        print("No available of student request in still pending\nReturn to home page\n")
        return
    for stud_request_info_pending in stud_request_list_pending:
        print(f"Request No.: {stud_request_info_pending[0]}\nStudent ID: {stud_request_info_pending[1]}\n"
              f"Change subject enrollment from {stud_request_info_pending[2]} to "
              f"{stud_request_info_pending[3]}\nReason: {stud_request_info_pending[4]}\n" + "~" * 70)
    return 1


def update_stud():
    # View all student's request which for changing subject enrolment
    # Ask receptionist to enter request no. and Ask receptionist to enter approve or reject the request
    # Not allow to enter request no. which does not exist
    # if approve then update the subject enrolment of student automatically based on the request and mark the request status as approved
    # if reject then mark the request status as rejected
    print("\nHome Page >>> View Student's Request and Update Student Enrollment Subject")
    print("-" * 30 + "View Student's Request and Update Student Enrollment Subject" + "-" * 30)
    if not view_stud_request():
        return
    if return_home_page("update student information"):
        return
    while True:
        request_no = input("Enter the Request No. to approve or reject the request: ").strip()
        if request_no.isdigit():
            request_info_request_no = find_one("request.txt", 0, 1, request_no)
            if request_info_request_no:
                break
        print("Invalid Request No.")
        if return_home_page("re-enter the request no."):
            return
    stud_id = request_info_request_no[1]
    change_subject = request_info_request_no[2]
    new_subject = request_info_request_no[3]
    stud_info_id = find_one("stud.txt", 0, 1, stud_id)
    change_subject_column = stud_info_id.index(change_subject)
    while True:
        approve_reject = input(
            "Enter APPROVE to approve the request / Enter REJECT to reject the request: ").strip().upper()
        if approve_reject in ["APPROVE", "REJECT"]:
            break
        else:
            print("You can only enter APPROVE or REJECT")
            if return_home_page("re-enter APPROVE or REJECT"):
                return
    if approve_reject == "APPROVE":
        edit("stud.txt", 0, 1, stud_id, change_subject_column, new_subject)
        edit("request.txt", 0, 1, request_no, 5, "APPROVED")
        print("-" * 30 + "\nStudent's Request approved and Update Student Enrollment Subject Success\n" + "-" * 30 +
              "\nReturn to home page\n")
    else:
        edit("request.txt", 0, 1, request_no, 5, "REJECTED")
        print("-" * 30 + "\nStudent's Request rejected\n" + "-" * 30 + "\nReturn to home page\n")


def generate_stud_payment():
    # Ask receptionist to enter 0 to generate all student's education fee bill for this mont
    print("\nHome Page >>> Generate Student Payment")
    print("-" * 30 + "Generate Student Payment" + "-" * 30)
    if return_home_page("generate all student education fee list in this month"):
        return
    stud_list = read_all("stud.txt")
    date_of_generate_education_fee = datetime.now().strftime("%B %Y")
    for stud_info in stud_list:
        stud_id = stud_info[0]
        stud_level = stud_info[8]
        payment_date = "NULL"
        subject1 = stud_info[9]
        subject2 = stud_info[10]
        subject3 = stud_info[11]
        subject1_fee = str(retrieve_subjects_fee(subject1))
        subject2_fee = str(retrieve_subjects_fee(subject2))
        subject3_fee = str(retrieve_subjects_fee(subject3))
        payment_status = "UNPAID"
        accept_payment_by = "NULL"
        new_payment_info = [stud_id, date_of_generate_education_fee, stud_level, payment_date, subject1, subject2,
                            subject3, subject1_fee, subject2_fee, subject3_fee, payment_status, accept_payment_by]
        register("payment.txt", new_payment_info)
    print("-" * 30 + "\nGenerate Student Payment Success\n" + "-" * 30 + "\nReturn to home page\n")


def view_student_payment_in_unpaid():
    # Display all student payment which in unpaid status
    stud_payment_list_unpaid = find_more("payment.txt", 10, 11, "UNPAID")
    if not stud_payment_list_unpaid:
        print("Unavailable of student unpaid payment")
        return
    stud_payment_list_unpaid.sort(key=lambda id: (id[0], ""))
    # View all student payment information which in unpaid status
    for stud_payment_info_unpaid in stud_payment_list_unpaid:
        print(f"Student ID: {stud_payment_info_unpaid[0]}\nMonth: {stud_payment_info_unpaid[1]}\n"
              f"Level: {stud_payment_info_unpaid[2]}\nPayment Detail: "
              f"Subject 1 {stud_payment_info_unpaid[4]} (RM{stud_payment_info_unpaid[7]}) | "
              f"Subject 2 {stud_payment_info_unpaid[5]} (RM{stud_payment_info_unpaid[8]}) | "
              f"Subject 3 {stud_payment_info_unpaid[6]} (RM{stud_payment_info_unpaid[9]})\n"
              f"Payment Status: {stud_payment_info_unpaid[10]}\n" + "~" * 100)
    return stud_payment_list_unpaid


def accept_payment(user_id):
    # when student already pay for their education, receptionist update the payment information by entering student id, the month and year pay for
    print("\nHome Page >>> Accept payment")
    print("-" * 30 + "Accept Payment" + "-" * 30)
    stud_payment_list_unpaid = view_student_payment_in_unpaid()
    if not stud_payment_list_unpaid:
        return
    if return_home_page("accept payment"):
        return
    stud_id = get_and_verify_stud_id_in_payment_file("accept the payment")
    if not stud_id:
        return
    month = get_and_verify_month()
    year = get_and_verify_year()
    if not month or not year:
        return
    date = f"{month} {year}"
    stud_payment_list_id = find_more("payment.txt", 0, 1, stud_id)
    stud_payment_list_date = find_more("payment.txt", 1, 2, date)
    stud_payment_list_id_date_unpaid = None
    for stud_payment_info_unpaid in stud_payment_list_unpaid:
        if stud_payment_info_unpaid in stud_payment_list_date and stud_payment_info_unpaid in stud_payment_list_id:
            stud_payment_list_id_date_unpaid = stud_payment_info_unpaid
    if not stud_payment_list_id_date_unpaid:
        print("Unavailable of student payment which contain required ID, Month and Year")
        return
    else:
        payment_date = datetime.now().strftime("%d %B %Y")
    recep_name = find_one("recep.txt", 0, 1, user_id)[2]
    edit("payment.txt", 0, 2, f"{stud_id},{date}", 11, recep_name)
    edit("payment.txt", 0, 2, f"{stud_id},{date}", 3, payment_date)
    edit("payment.txt", 0, 2, f"{stud_id},{date}", 10, "PAID")
    print("-" * 30 + "\nAccept Payment Success\n" + "-" * 30 + "\nReturn to home page\n")


def generate_receipt():
    # Receptionist can generate payment receipt of student
    # Enter student id, the month and year of payment
    print("\nHome Page >>> Generate Receipt")
    print("-" * 30 + "Generate Receipt" + "-" * 30)
    stud_payment_list_paid = find_more("payment.txt", 10, 11, "PAID")
    if not stud_payment_list_paid:
        print("No available of Student Payment which in paid status\nReturn to home page\n")
        return
    stud_id = get_and_verify_stud_id_in_payment_file("generate the receipt")
    if not stud_id:
        return
    month = get_and_verify_month()
    year = get_and_verify_year()
    if not month or not year:
        return
    date = f"{month} {year}"
    stud_payment_list_id = find_more("payment.txt", 0, 1, stud_id)
    stud_payment_list_date = find_more("payment.txt", 1, 2, date)
    stud_payment_list_id_date_paid = None
    for stud_payment_info_paid in stud_payment_list_paid:
        if stud_payment_info_paid in stud_payment_list_date and stud_payment_info_paid in stud_payment_list_id:
            stud_payment_list_id_date_paid = stud_payment_info_paid
    if not stud_payment_list_id_date_paid:
        print(
            "\nNo available of student payment which contain required ID, Month and Year and Status\nReturn to home page\n")
        return
    else:
        total_amount_paid = 0
        for amount_paid in stud_payment_list_id_date_paid[7:10]:
            total_amount_paid += int(amount_paid)
    stud_info_id = find_one("stud.txt", 0, 1, stud_id)
    print("~" * 30 + "Student Receipt" + "~" * 30)
    print(f"Student ID: {stud_payment_list_id_date_paid[0]}\nStudent Name: {stud_info_id[2]}\n"
          f"Month of Education fee: {stud_payment_list_id_date_paid[1]}\n"
          f"Payment Date: {stud_payment_list_id_date_paid[3]}\nTotal Amount: RM{total_amount_paid}"
          f"\nAccept payment by Receptionist: {stud_payment_list_id_date_paid[11]}\n")
    print("Student's Receipt Generated\nReturn to home page\n")


def delete_stud():
    # Display all student account's information before deleting
    # Ask receptionist to enter student's id to delete account
    # Not allow to enter student's id which does not exist
    print("\nHome Page >>> Delete Student")
    print("-" * 30 + "Delete Student" + "-" * 30)
    stud_info_list = ["Student's ID", "Student's Password", "Student's Name", "Student's IC or Passport",
                      "Student's Address", "Student's Email", "Student's Contact Number", "Month of Enrollment"]
    stud_list = read_all("stud.txt")
    if not stud_list:
        print("No student information")
        return
    stud_list.sort(key=lambda id: (id[0], "stud"))
    for stud_info in stud_list:
        for index, stud_data in enumerate(stud_info[0:8]):
            if index != 1:
                print(f"{stud_info_list[index]}: {stud_data}")
        print("~" * 70)
    if return_home_page("delete student's account"):
        return
    while True:
        stud_id = input("Please enter student id to delete the account: ")
        stud_info_id = find_one("stud.txt", 0, 1, stud_id)
        if stud_info_id:
            delete_row = stud_list.index(stud_info_id)
            break
        else:
            print("This student id does not exist")
            if return_home_page("re-enter the student's id"):
                return
    delete("stud.txt", delete_row)
    print("-" * 30 + "\nDelete Student Information Success\n" + "-" * 30 + "\nReturn to home page\n")


def add_news():
    # receptionist can add news related to tuition centre in this function
    print("\nHome Page >>> Add News")
    print("-" * 30 + "Add News" + "-" * 30)
    new_news_str = ""
    num = 1
    print("You can add tuition center news (Enter NULL if no more news)")
    while True:
        news_data = input(f"Paragraph {num}: ")
        if news_data.upper() == "NULL":
            break
        else:
            new_news_str += news_data + "\\n"
            num += 1
    new_news_list = [new_news_str]
    register("news.txt", new_news_list)
    print("-" * 30 + "\nAdd News Success\n" + "-" * 30 + "\nReturn to home page\n")


def delete_news():
    # receptionist can delete news related to tuition centre in this function
    print("\nHome Page >>> Delete News")
    print("-" * 30 + "Delete News" + "-" * 30)
    if not view_news():
        print("No any news")
        return
    if return_home_page("delete news"):
        return
    while True:
        delete_news_num = input("Please enter the News No. that you would like to delete: ")
        try:
            delete_news_num = int(delete_news_num)
            if 0 < delete_news_num <= len(read_all("news.txt")):
                break
            else:
                print("Invalid news no")
        except ValueError:
            print("Invalid news no")
        if return_home_page("re-enter the News Number"):
            return
    delete("news.txt", delete_news_num - 1)
    print("-" * 30 + "\nDelete News Success\n" + "-" * 30 + "\nReturn to home page\n")


# -----------------------------------------End Receptionist functionality-----------------------------------------------

# The following code done by Wong Jin Wei
# -----------------------------------------------Tutor functionality----------------------------------------------------
def tutor_ui(user_id):
    # Direct tutor to this function when login success
    # Display all functionality to tutor
    # Ask tutor to choose function
    tutor_functions = ["Add class information", "Update class information", "Delete Class Information",
                       "View Student List in the Subject", "Change Password", "Update Profile", "Log out"]
    while True:
        print("-" * 30 + "Tutor Home Page" + "-" * 30)
        for index, function in enumerate(tutor_functions):
            print(f"Enter {index + 1}: {function}")
        choice = input("Enter number: ")
        if choice == "1":
            add_class(user_id)
        elif choice == "2":
            update_class(user_id)
        elif choice == "3":
            delete_class(user_id)
        elif choice == "4":
            view_stud(user_id)
        elif choice == "5":
            change_password("tutor.txt", user_id)
        elif choice == "6":
            update_profile("tutor.txt", user_id)
        elif choice == "7":
            print("Log out success\n")
            return "out"
        else:
            print("Invalid command")


def add_class(user_id):
    # Tutor allow to add class schedule for assigned level and assigned subject
    print("\nHome Page >>> Add Class Schedule")
    print("-" * 30 + "Add Class Schedule" + "-" * 30)
    tutor_info = find_one("tutor.txt", 0, 1, user_id)
    tutor_name = tutor_info[2]
    tutor_assign_level = tutor_info[7]
    tutor_assign_subject = tutor_info[8]
    subject_charge = str(retrieve_subjects_fee(tutor_assign_subject))
    class_date = get_and_verify_class_date()
    if not class_date:
        return
    class_venue = get_and_verify_class_venue()
    if not class_venue:
        return
    class_start_time = get_and_verify_class_time("Start")
    if not class_start_time:
        return
    class_end_time = get_and_verify_class_time("End")
    if not class_end_time:
        return
    new_class_info = [class_date, class_venue, class_start_time, class_end_time, tutor_assign_level,
                      tutor_assign_subject, subject_charge, tutor_name, user_id]
    register("class.txt", new_class_info)
    print("-" * 30 + "\nClass information has been saved\n" + "-" * 30 + "\nReturn to home page\n")


def tutor_view_class(user_id):
    # Allow tutor to view all class schedule which conducted by him/her
    class_info_list = ["Date", "Venue", "Start time", "End time", "Level", "Subject", "Charge", "Tutor name",
                       "Tutor id"]
    tutor_class_list = find_more("class.txt", 8, None, user_id)
    if not tutor_class_list:
        print("No class schedule")
        return
    tutor_class_list.sort(
        key=lambda date: (datetime.strptime(date[0], "%d %B %Y"), datetime.strptime(date[2], "%H.%M %p")))
    for index, tutor_class in enumerate(tutor_class_list):
        tutor_class_str = ""
        tutor_class_str += f"(Class No. {index + 1})"
        for class_data_num, class_data in enumerate(class_info_list):
            tutor_class_str += f"\n{class_data}: {tutor_class[class_data_num]}"
        tutor_class_str += "\n" + "~" * 70
        print(tutor_class_str)
    return tutor_class_list


def update_class(user_id):
    # Display the class schedule
    # Ask tutor to enter class schedule no. to update the class schedule
    # Updating the class schedule by entering the type of class information and new information
    print("\nHome Page >>> Update Class Information")
    print("-" * 30 + "Update Class Information" + "-" * 30)
    class_list = tutor_view_class(user_id)
    class_info_list = ["Date", "Venue", "Start time", "End time", "Level", "Subject", "Charge", "Tutor name",
                       "Tutor id"]
    if not class_list:
        return
    if return_home_page("update class schedule"):
        return
    while True:
        update_choice = input("Please enter Class No. to update the class information: ")
        try:
            update_choice = int(update_choice)
            if 0 < update_choice <= len(class_list):
                chosen_class = class_list[update_choice - 1]
                break
            else:
                print("\nClass No. does not exist!!!")
                if return_home_page("re-enter the class no."):
                    return
        except ValueError:
            print("\nClass No. does not exist!!!")
            if return_home_page("re-enter the class no."):
                return
    while True:
        class_data = input("Please enter one class information to edit the information (exp: Date): ").capitalize()
        if class_data in class_info_list[:4]:
            class_column = class_info_list.index(class_data)
            break
        elif class_data in class_info_list[4:]:
            print("\nYou cannot update this information\nPlease enter again")
        else:
            print("Invalid class information!!!")
            if return_home_page("re-enter the class information"):
                return
    if class_data == "Date":
        new_data = get_and_verify_class_date()
    elif class_data == "Venue":
        new_data = get_and_verify_class_venue()
    elif class_data == "Start Time":
        new_data = get_and_verify_class_time("Start")
    else:
        new_data = get_and_verify_class_time("End")
    if not new_data:
        return
    chosen_class_str = ",".join(chosen_class)
    edit("class.txt", 0, None, chosen_class_str, class_column, new_data)
    print("-" * 30 + "\nUpdate Class success\n" + "-" * 30 + "\nReturn to home page\n")


def delete_class(user_id):
    # Allow tutor to delete class schedule by entering class schedule no.
    print("\nHome Page >>> Delete Class Information")
    print("-" * 30 + "Delete Class Information" + "-" * 30)
    class_list = tutor_view_class(user_id)
    if not class_list:
        return
    if return_home_page("delete class schedule"):
        return
    while True:
        # Prompt user for choose the class that would like to update
        delete_choice = input("Please enter Class No. to delete the class information: ")
        try:
            delete_choice = int(delete_choice)
            # Identity the validity of class no.
            if 0 < delete_choice <= len(class_list):
                break
            else:
                print("\nClass No. does not exist!!!")
                if return_home_page("re-enter the class no."):
                    return
        except ValueError:
            print("\nClass No. does not exist!!!")
            if return_home_page("re-enter the class no."):
                return
    chosen_class = class_list[delete_choice - 1]
    for class_row, class_list in enumerate(read_all("class.txt")):
        if chosen_class == class_list:
            delete_row = class_row
            delete("class.txt", delete_row)
            print("-" * 30 + "\nDelete Class Information Success\n" + "-" * 30 + "\nReturn to home page\n")
            break


def view_stud(user_id):
    # Display all student who in the tutor's class
    print("\nHome Page >>> View Student List in the Subject")
    print("-" * 30 + "View Student List in the Subject" + "-" * 30)
    print("-" * 8 + "(Student List)" + "-" * 8)
    tutor_info = find_one("tutor.txt", 0, 1, user_id)
    assign_level = tutor_info[7]
    assign_subject = tutor_info[8]
    stud_list_assign_level = find_more("stud.txt", 8, 9, assign_level)
    stud_list = read_all("stud.txt")
    stud_list_assign_subject = []
    for stud_information in stud_list:
        if assign_subject in stud_information[9:]:
            stud_list_assign_subject.append(stud_information)
    if not stud_list_assign_level or not stud_list_assign_subject:
        print("No student in this class\n" + "\nReturn teo home page\n")
        return
    for stud_info_assign_subject in stud_list_assign_subject:
        if stud_info_assign_subject in stud_list_assign_level:
            print(f"Student ID: {stud_info_assign_subject[0]}  |  Student Name: {stud_info_assign_subject[2]}")
    print("\nReturn to home page\n")


# ---------------------------------------------End Tutor functionality--------------------------------------------------

# The following code done by Wong Jin Wei
# ----------------------------------------------Student functionality---------------------------------------------------
def stud_ui(user_id):
    # Direct student to this function when login success
    # Display all functionality to student
    # Ask student to choose function
    stud_functions = ["View Schedule", "Send Request", "View and Delete Request", "View Payment", "Change Password",
                      "Update Profile", "Log out"]
    while True:
        print("------------------------Student Home Page------------------------")
        for index, function in enumerate(stud_functions):
            print(f"Enter {index + 1}: {function}")
        choice = input("Enter number: ")
        if choice == "1":
            stud_view_class(user_id)
        elif choice == "2":
            send_request(user_id)
        elif choice == "3":
            delete_request(user_id)
        elif choice == "4":
            view_payment(user_id)
        elif choice == "5":
            change_password("stud.txt", user_id)
        elif choice == "6":
            update_profile("stud.txt", user_id)
        elif choice == "7":
            print("Log out success\n")
            return "out"
        else:
            print("Invalid command, please try again")


def stud_view_class(user_id):
    # Display all class schedule related to the student's enrolled level and subjects
    print("\nHome Page >>> View Class Schedule")
    print("-" * 30 + "Class Schedule" + "-" * 30)
    stud_info_id = find_one("stud.txt", 0, 1, user_id)
    stud_level = stud_info_id[8]
    stud_subjects = stud_info_id[9:]
    stud_class_list_level_subjects = []
    for stud_subject in stud_subjects:
        stud_class_list_level_subject = find_more("class.txt", 4, 6, f"{stud_level},{stud_subject}")
        if stud_class_list_level_subject:
            for stud_class_info_level_subject in stud_class_list_level_subject:
                stud_class_list_level_subjects.append(stud_class_info_level_subject)
    if not stud_class_list_level_subjects:
        print("-" * 30 + "\nNo Class Schedule\n" + "-" * 30 + "\nReturn to home page\n")
        return
    stud_class_list_level_subjects.sort(
        key=lambda date: (datetime.strptime(date[0], "%d %B %Y"), datetime.strptime(date[2], "%H.%M %p")))
    for stud_class_info_level_subjects in stud_class_list_level_subjects:
        print(f"Date: {stud_class_info_level_subjects[0]}\n"
              f"Venue: {stud_class_info_level_subjects[1]}\n"
              f"Time: From {stud_class_info_level_subjects[2]} "
              f"to {stud_class_info_level_subjects[3]}\n"
              f"Level: {stud_class_info_level_subjects[4]}\n"
              f"Subject: {stud_class_info_level_subjects[5]}\n"
              f"Charge: {stud_class_info_level_subjects[6]}\n"
              f"Lecturer: {stud_class_info_level_subjects[7]}\n" + "~" * 30)
    print("\nReturn to home page\n")

# The following code done by Wong Jin Wei
def send_request(user_id):
    # Allow student to send request to receptionist for changing subject enrolment by entering current subject, new subject and reason
    print("\nHome Page >>> Send Request")
    print("-" * 30 + "Send Request" + "-" * 30)
    view_levels_and_subjects()
    stud_info = find_one("stud.txt", 0, 1, user_id)
    stud_level = stud_info[8]
    subjects_list = retrieve_level_or_subject("subjects", stud_level)
    current_subjects = stud_info[9:]
    print(
        f"(Your current enrolled subject)\nSubject 1: {current_subjects[0]}\nSubject 2: {current_subjects[1]}\nSubject 3: {current_subjects[2]}")
    if return_home_page("send request"):
        return
    while True:
        ori_subject_num = input("\nEnter the subject number that you want to change (exp: 1/2/3): ")
        try:
            ori_subject_num = int(ori_subject_num)
            if ori_subject_num in range(1, 4):
                ori_subject = current_subjects[ori_subject_num - 1]
                break
            else:
                print("\nYou must write in 1, 2 or 3 only")
                if return_home_page("re-enter the subject number"):
                    return
        except ValueError:
            print("\nYou must write in 1, 2 or 3 only")
            if return_home_page("re-enter the subject number"):
                return
    while True:
        change_subject = input("Enter subject name that want to change to: ").upper()
        if change_subject in subjects_list and change_subject not in current_subjects:
            break
        else:
            print("\nInvalid subject\nPlease enter valid subject")
            if return_home_page("re-enter the subject name"):
                return
    reason = input("Please provide suitable reason for changing subject: ")
    request_list = read_all("request.txt")
    if not request_list:
        current_request_no = "1"
    else:
        request_no = int(request_list[-1][0]) + 1
        current_request_no = str(request_no)
    request_info = [current_request_no, user_id, ori_subject, change_subject, reason, "STILL PENDING"]
    register("request.txt", request_info)
    print("-" * 30 + "\nRequest has sent to receptionist\n" + "-" * 30 + "\nReturn to home page\n")


def delete_request(user_id):
    # Allow student to delete request which in still pending status by entering Request No
    print("\nHome Page >>> Delete Request")
    print("-" * 30 + "View and Delete Request" + "-" * 30)
    stud_request_list = find_more("request.txt", 1, 2, user_id)
    if not stud_request_list:
        print("You have no send any request")
        return
    else:
        for request_info in stud_request_list:
            print(f"Request No.: {request_info[0]}\nStudent ID: {request_info[1]}\nFrom Subject: "
                  f"{request_info[2]}\nChange to Subject: {request_info[3]}\nReason: "
                  f"{request_info[4]}\nRequest Status: {request_info[5]}\n" + "~" * 30)
    if return_home_page("delete request"):
        return
    while True:
        delete_line = input("Please enter Request No. for deletion: ")
        if delete_line.isdigit():
            request_info_request_no = find_one("request.txt", 0, 1, delete_line)
            if request_info_request_no:
                if request_info_request_no[-1] == "STILL PENDING":
                    break
                else:
                    print("You cannot delete this request because it already approved or rejected")
                    if return_home_page("re-enter the request No."):
                        return
            else:
                print("Request No. does not exist")
                if return_home_page("re-enter the request no."):
                    return
        else:
            print("Invalid Request No.")
            if return_home_page("re-enter the request no."):
                return
    delete_row = int(delete_line) - 1
    delete("request.txt", delete_row)
    print("-" * 30 + "\nDelete request success\n" + "-" * 30 + "\nReturn to home page\n")

# The following code done by Lew Wai How
def view_payment(user_id):
    # Allow student to view his/her education fee bill which have not pay yet
    print("\nHome Page >>> View Payment")
    print("-" * 30 + "View Payment" + "-" * 30)
    payment_list_id = find_more("payment.txt", 0, 1, user_id)
    payment_list_unpaid = find_more("payment.txt", 10, 11, "UNPAID")
    payment_list_id_unpaid = []
    if not payment_list_unpaid:
        print("No payment need to paid")
        return
    else:
        for payment_info_unpaid in payment_list_unpaid:
            if payment_info_unpaid in payment_list_id:
                payment_list_id_unpaid.append(payment_info_unpaid)
    for payment_info_id_unpaid in payment_list_id_unpaid:
        subject1_fee = payment_info_id_unpaid[7]
        subject2_fee = payment_info_id_unpaid[8]
        subject3_fee = payment_info_id_unpaid[9]
        payable = int(subject1_fee) + int(subject2_fee) + int(subject3_fee)
        print(f"Date: {payment_info_id_unpaid[1]}\nLevel: {payment_info_id_unpaid[2]}\n"
              f"Payment Status: {payment_info_id_unpaid[10]}\n"
              f"Payment Detail: Subject 1 {payment_info_id_unpaid[4]} (RM{subject1_fee})"
              f" | Subject 2 {payment_info_id_unpaid[5]} (RM{subject2_fee})"
              f" | Subject 3 {payment_info_id_unpaid[6]} (RM{subject3_fee})\n"
              f"Payable: RM{payable}\n" + "~" * 70)
    print("\nKindly remind: Please pay your education fee before the due date. Thank You\nReturn to home page\n")


# ----------------------------------------------End Tutor functionality-------------------------------------------------
# The following code done by Lew Wai How
# ----------------------------------------------------Main Page---------------------------------------------------------
def login():
    # User should enter id and password to login account
    # All user has only 3 chance for login except admin
    # If user enter wrong id or password, it cost one chance
    # Once used all chance, the program close
    roles_file = ["admin.txt", "recep.txt", "tutor.txt", "stud.txt"]
    login_num = 0
    while login_num < 3:
        user_id = input("Enter id: ").strip()
        for current_file in roles_file:
            user_info = find_one(current_file, 0, 1, user_id)
            if user_info:
                password = user_info[1]
                user_password = input("Enter password: ").strip()
                user_password_crypt = crypt_password(user_password)
                if user_password_crypt == password:
                    print("\nLogin success\nWelcome\n")
                    return [current_file, user_id]
                else:
                    print("Invalid Password")
                    if current_file == "admin.txt":
                        login_num = -1
                        print("\nInvalid password\nOnly Admin login failed will reset login chance")
                    break
        else:
            print("Invalid ID")
        login_num += 1
        print(f"You remain {3 - login_num} chance !!!\n")

# The following code done by Tan Po Yeh
def view_news():
    # Allow all user to view the news related to tuition centre
    print("-" * 30 + "View news" + "-" * 30)
    with open("news.txt", "r") as news_file:
        news_info = news_file.readline()
        if not news_info:
            return False
        else:
            news_num = 1
            while news_info:
                print(f"News {news_num}\n")
                news = news_info.replace("\\n", "\n")
                print(news + "~" * 70)
                news_info = news_file.readline()
                news_num += 1
            return True

# The following code done by Lew Wai How
def main():
    # This is the first page when user open the program
    # Ask enter 1 for login account or enter 2 for viewing news related to tuition centre
    while True:
        print("-" * 30 + "Welcome to Brilliant Education Center" + "-" * 30 + "\n")
        print("Enter 1: Login account\nEnter 2: View news")
        while True:
            choice = input("\nEnter a number: ")
            if choice == "1":
                print("\nPlease enter your id and password for login")
                user_login = login()
                if not user_login:
                    print("You have use all chance and not allow to login")
                    exit()
                elif user_login[0] == "admin.txt":
                    admin_ui(user_login[1])
                    break
                elif user_login[0] == "recep.txt":
                    recep_ui(user_login[1])
                    break
                elif user_login[0] == "tutor.txt":
                    tutor_ui(user_login[1])
                    break
                else:
                    stud_ui(user_login[1])
                    break
            elif choice == "2":
                print("\nMain page >>> View news")
                if not view_news():
                    print("No available of news")
                print("Return to main page\n")
                break
            else:
                print("Invalid command")


# --------------------------------------------------End Main Page-------------------------------------------------------

main()
