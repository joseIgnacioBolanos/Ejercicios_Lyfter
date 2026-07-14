import csv
from action import Student
def save_students(file_path, data):
    if data:
        list_of_students=[]
        for student in data:
            list_of_students.append(student.convert_to_dictionary())
        with open(file_path, 'w', encoding='utf-8', newline='') as file:

            headers = list_of_students[0].keys()

            writer = csv.DictWriter(file, fieldnames=headers)

            writer.writeheader()

            writer.writerows(list_of_students)

            print('Data successfully exported')
    else:
         print('Students list is empty')



def import_students_data(file_path):
    new_student_list=[]
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for student in reader: 
                student_object= Student.convert_dictionary_to_object(student)               
                new_student_list.append(student_object) 
        print('Data successfully imported')
        return new_student_list             
    except FileNotFoundError as e:
        print('ERROR! File not found')
        return new_student_list

