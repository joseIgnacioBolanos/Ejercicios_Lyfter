import csv

def save_students(file_path, data):
    if data:
        with open(file_path, 'w', encoding='utf-8', newline='') as file:

            headers = data[0].keys()

            writer = csv.DictWriter(file, fieldnames=headers)

            writer.writeheader()

            writer.writerows(data)
    else:
         print('Lista de estudinates vacia')



def import_students_data(file_path):
    new_student_list=[]
    temp_grade=0
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for student in reader: 
                for subject, grade in student.items():
                            if subject=='Name' or subject=='Section'or subject=='Average Grade':
                                continue
                            else:
                                temp_grade= int(grade)
                                student[subject]=temp_grade
                new_student_list.append(student) 
        return new_student_list             
    except FileNotFoundError:
        print('Aun no existe el archivo que deseas abrir')

