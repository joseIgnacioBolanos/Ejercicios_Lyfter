def adding_student_data(students_list):
    while True:
        my_student={}
        name=''
        section= ''
        spanish_grade=0
        english_grade=0
        socials_grade=0
        science_grade=0
        average_grade=0.0
        
        name=is_valid_name("Enter the student's name ")
        section=is_valid_section("Enter the student's section. Follow the correct format (ex: 10A, 11B, etc.)")
        if student_exists(name, section, students_list):
            continue
        english_grade=validating_grade_input("Enter the English Grade: ")
        spanish_grade=validating_grade_input('Enter the Spanish Grade ')
        socials_grade=validating_grade_input('Enter the Social Studies Grade ')
        science_grade=validating_grade_input('Enter the Science Grade ')
        
        my_student['Name']= name
        my_student['Section']=section
        my_student['English Grade']=english_grade
        my_student['Spanish Grade']=spanish_grade
        my_student['Socials Grade']=socials_grade
        my_student['Science Grade']=science_grade
        average_grade = (my_student['English Grade'] + my_student['Spanish Grade'] + my_student['Socials Grade'] + my_student['Science Grade']) / 4
        my_student['Average Grade']= average_grade

        students_list.append(my_student)

        
        while True:
            user_option= is_valid_int('Enter:\n1. To continue adding new students.\n2. To return to the main menu\n')
            if user_option == 2:
                return students_list
            elif user_option==1:
                break
            else:
                if user_option !=2 or user_option != 1:
                    print('Invalid Option')
            

def is_valid_section(message):
    while True:
        section= input(message).strip()
        if len(section) == 2:
         if section[0].isdigit() and section[1].isalpha():
            return section.upper()
         else:
             print('Invalid input value')
        elif len(section)== 3:
            if section[0].isdigit() and section[1].isdigit() and section[2].isalpha():
               return section.upper()
            else:
                print('Invalid input value')
        else:
            print('Invalid input value')


def is_valid_name(message):
    while True:
        user_input=input(message).strip()
        if not user_input:
            valid =False
        else:    
            words=user_input.split()
            valid =True
            for word in words:
                if not word.isalpha():
                    valid =False

        if valid:
            return user_input.title()
        else:
            print('Invalid input value')


def validating_grade_input(message):
    while True:
        user_input=input(message)
        try:
            user_input_int= int(user_input)
            if user_input_int >= 0 and user_input_int <=100:
                return user_input_int
            else:
                print('ERROR! The grade must be between 0 and 100')
        except ValueError:
            print('Invalid input value')


def is_valid_int(message):
    while True:
        user_input= input(message)
        try:
            user_input_int= int(user_input)
            return user_input_int
        except ValueError:
            print('Invalid input value')


def print_student_data(student_data):
    if student_data:
        for student in student_data:
            print(f"Student: {student['Name']}\nSection: {student['Section']}\nEnglish Grade {student['English Grade']}\nSpanish Grade {student['Spanish Grade']}\nSocials Studies Grade: {student['Socials Grade']}\nScience Grade: {student['Science Grade']}")
            print('\n')
    else:
        return print('Students list is empty')


def top_three_students(student_data):
    if student_data:
        new_student_data=[]
        for students in  student_data:
            new_student_data.append(students)

        top_three=[]
        
        while len(top_three)< 3 and new_student_data:
            higher= new_student_data[0]
            found_higher=0
            index_to_be_removed= 0
            for student in new_student_data:
                if higher['Average Grade'] < student['Average Grade']:
                    higher=student
                    index_to_be_removed=found_higher
                found_higher+=1
            top_three.append(higher)
            new_student_data.pop(index_to_be_removed)
        
        print(f"Top 3 students with the highest average grade:")
        for student in top_three:
            print(f"Student:{student['Name']}\n")
    else:
        return print('Students list is empty')
    

def print_average_grades(student_data):
    if student_data:
        class_average_grade=0.0
        for student in student_data:
            class_average_grade+=student['Average Grade']
        class_average_grade = class_average_grade // len(student_data)
        print(f'The average grade is {class_average_grade}')
    else:
        return print('Students list is empty')


def remove_student(student_data):
    if student_data:
        counter=0
        index_to_be_removed= 0
        not_found=True
        student_name=is_valid_name("Enter the student's name to be removed ")
        student_section=is_valid_section("Enter the student's section: ")
        for student in student_data:
            if student['Name'] == student_name and student['Section']== student_section:
                user_answer = is_valid_int(f"Are you sure you want to remove {student['Name']}. Section: {student['Section']}? Enter:\n1. Yes\n2. No\n")
                if user_answer== 1:
                    index_to_be_removed=counter
                    student_data.pop(index_to_be_removed)
                    not_found=False
                    print(f'Student {student_name} from Section {student_section} was successfully removed')
                    break
                elif user_answer==2:
                    not_found=False
                    break
                else:
                    print('Invalid input value. Returning to the main menu...')
                    not_found=False
                    break
            counter+=1

        if not_found: 
                print(f"Student {student_name} from section {student_section} doesn't exist")
    else:
        return print('Students list is empty')


def student_exists(student_name, student_section, students_list):
    if students_list:
        for student in students_list:
            if student['Name']==student_name and student['Section']== student_section:
                print(f"ERROR! The student {student_name} from section: {student_section} already exist. Please enter a new student \n")
                return True


def failed_student_list(students_list):
    if students_list:
        failed_students=[]
        if students_list:
            for student in students_list:
                is_failed=False
                my_student={}
                for subject, grade in student.items():
                    if subject=='Name' or subject=='Section' or subject=='Average Grade':
                        continue
                    elif grade < 60:
                        my_student[subject] = grade
                        is_failed=True
                        
                if is_failed:
                    my_student['Name']= student['Name']
                    my_student['Section']= student['Section']
                    failed_students.append(my_student)

            if failed_students:
                for student in failed_students:
                            print(f"Name: {student['Name']}\nSection: {student['Section']}")
                            print('Failed Curses:')
                            for subject, grade in student.items():
                                if subject=='Name' or subject=='Section' or subject=='Average Grade':
                                    continue
                                else:
                                    print(f"{subject}: {grade} ")
                            print('\n')
            else:
                print("No failed students found")
    else:
        return print("Students list is empty")

            



