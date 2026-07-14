class Student():
    def __init__(self, name, section, spanish_grade, english_grade, socials_grade, science_grade):
        self.name = name
        self.section = section
        self.spanish_grade =  spanish_grade
        self.english_grade = english_grade
        self.socials_grade = socials_grade
        self.science_grade = science_grade

    def calculating_average_grade(self):
        average_grade= (self.english_grade + self.spanish_grade + self.socials_grade + self.science_grade) / 4
        return average_grade
    
    def convert_to_dictionary(self):
        my_dictionary={}
        my_dictionary['Name']= self.name
        my_dictionary['Section']=self.section
        my_dictionary['English Grade']= self.english_grade
        my_dictionary['Spanish Grade']= self.spanish_grade
        my_dictionary['Socials Grade']= self.socials_grade
        my_dictionary['Science Grade'] = self.science_grade

        return my_dictionary
    
    def convert_dictionary_to_object(student_dictionary):
        
            my_student=Student(student_dictionary['Name'], student_dictionary['Section'], int(student_dictionary['Spanish Grade']),int(student_dictionary['English Grade']), int(student_dictionary['Socials Grade']),int(student_dictionary['Science Grade'] ))
            
            return my_student


def adding_student_data(students_list):
    while True:
        name=is_valid_name("Enter the student's name ")
        section = is_valid_section("Enter the student's section. Follow the correct format (ex: 10A, 11B, etc.)")
        if student_exists(name, section, students_list):
            continue
        english_grade = validating_grade_input("Enter the English Grade: ")
        spanish_grade = validating_grade_input('Enter the Spanish Grade ')
        socials_grade = validating_grade_input('Enter the Social Studies Grade ')
        science_grade = validating_grade_input('Enter the Science Grade ')
        
        student = Student(name, section,  spanish_grade, english_grade, socials_grade, science_grade)

        students_list.append(student)

        
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
            print(f"Student: {student.name}\nSection: {student.section}\nEnglish Grade {student.english_grade}\nSpanish Grade {student.spanish_grade}\nSocials Studies Grade: {student.socials_grade}\nScience Grade: {student.science_grade}")
            print('\n')
    else:
        print('Students list is empty')


def top_three_students(student_data):
    if student_data:
        new_student_data= student_data.copy()
        top_three=[]
        
        while len(top_three)< 3 and new_student_data:

            higher= new_student_data[0]
            found_higher=0
            index_to_be_removed= 0

            higher_average_temp= higher.calculating_average_grade()

            for student in new_student_data:

                average_grade_temp= student.calculating_average_grade()
                if higher_average_temp < average_grade_temp:
                    higher=student
                    higher_average_temp= average_grade_temp
                    index_to_be_removed=found_higher
                found_higher+=1
            top_three.append(higher)
            new_student_data.pop(index_to_be_removed)
        
        print(f"Top 3 students with the highest average grade:")
        for student in top_three:
            print(f"Student:{student.name}\n")
    else:
        print('Students list is empty')
    

def print_average_grades(student_data):
    if student_data:
        class_average_grade=0.0
        for student in student_data:
            class_average_grade+=(student.english_grade + student.spanish_grade + student.socials_grade + student.science_grade) / 4
        class_average_grade = class_average_grade / len(student_data)
        print(f'The average grade is {class_average_grade}')
    else:
        print('Students list is empty')


def remove_student(student_data):
    if student_data:
        counter=0
        index_to_be_removed= 0
        not_found=True
        student_name=is_valid_name("Enter the student's name to be removed ")
        student_section=is_valid_section("Enter the student's section: ")
        for student in student_data:
            if student.name == student_name and student.section== student_section:
                user_answer = is_valid_int(f"Are you sure you want to remove {student.name}. Section: {student.section}? Enter:\n1. Yes\n2. No\n")
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
        print('Students list is empty')


def student_exists(student_name, student_section, students_list):
    if students_list:
        for student in students_list:
            if student.name==student_name and student.section== student_section:
                print(f"ERROR! The student {student_name} from section: {student_section} already exist. Please enter a new student \n")
                return True


def failed_student_list(students_list):
    if students_list:
        failed_student_found= False
        for student in students_list:
            if student.english_grade < 60 or student.spanish_grade < 60 or student.socials_grade < 60 or student.science_grade < 60:
                            failed_student_found=True
                            print(f"Name: {student.name}\nSection: {student.section}")
                            print('Failed Courses:')
                            if student.english_grade < 60:
                                print(f"English: {student.english_grade}")
                            if student.spanish_grade < 60:
                                print(f"Spanish: {student.spanish_grade}")
                            if student.socials_grade < 60:
                                print(f"Socials Studies: {student.socials_grade}")
                            if student.science_grade < 60:
                                print(f"Science: {student.science_grade}")
            
        if not failed_student_found:
            print("No failed students found")
    else:
        print("Students list is empty")

            



