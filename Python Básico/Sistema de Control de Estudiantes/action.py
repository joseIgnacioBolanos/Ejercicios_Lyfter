def addingStudentData(students_list):
    while True:
        my_student={}
        name=''
        section= ''
        spanishGrade=0
        englishGrade=0
        socialsGrade=0
        scienceGrade=0
        average_grade=0.0
        
        name=is_valid_name('Digite el nombre del Estudiante ')
        section=is_valid_section('Digite la sección del Estudiante, siga el formato válido (ejemplo: 10A, 11B, etc.)')
        if student_exists(name, section, students_list):
            continue
        englishGrade=validating_grade_input('Digite la nota de Ingles del Estudiante ')
        spanishGrade=validating_grade_input('Digite la nota de Español del Estudiante ')
        socialsGrade=validating_grade_input('Digite la nota de Sociales del Estudiante ')
        scienceGrade=validating_grade_input('Digite la nota de Ciencias del Estudiante ')
        
        my_student['Name']= name
        my_student['Section']=section
        my_student['English Grade']=englishGrade
        my_student['Spanish Grade']=spanishGrade
        my_student['Socials Grade']=socialsGrade
        my_student['Science Grade']=scienceGrade
        average_grade = (my_student['English Grade'] + my_student['Spanish Grade'] + my_student['Socials Grade'] + my_student['Science Grade']) / 4
        my_student['Average Grade']= average_grade

        students_list.append(my_student)

        
        while True:
            userOption= is_valid_int('Digite:\n1. Para continuar agregando mas Estudiantes.\n2. Para volver al menu Principal ')
            if userOption == 2:
                return students_list
            elif userOption==1:
                break
            else:
                if userOption !=2 or userOption != 1:
                    print('Valor ingresado incorrecto')
            

def is_valid_section(message):
    while True:
        section= input(message).strip()
        if len(section) == 2:
         if section[0].isdigit() and section[1].isalpha():
            return section.upper()
         else:
             print('Formato Invalido')
        elif len(section)== 3:
            if section[0].isdigit() and section[1].isdigit() and section[2].isalpha():
               return section.upper()
            else:
                print('Formato Invalido')
        else:
            print('Formato invalido')


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
            print('El valor ingresado es Invalido')


def validating_grade_input(message):
    while True:
        user_input=input(message)
        try:
            user_input_int= int(user_input)
            if user_input_int >= 0 and user_input_int <=100:
                return user_input_int
            else:
                print('ERROR! La nota debe de estar entre 0 y 100')
        except ValueError:
            print('Valor ingresado es Invalido')


def is_valid_int(message):
    while True:
        user_input= input(message)
        try:
            user_input_int= int(user_input)
            return user_input_int
        except ValueError:
            print('Valor ingresado no valido')


def printStudentData(student_data):
    if student_data:
        for student in student_data:
            print(f"Nombre del estudiante: {student['Name']}\nSección: {student['Section']}\nNota de Inglés {student['English Grade']}\nNota de Español {student['Spanish Grade']}\nNota de Sociales: {student['Socials Grade']}\nNota de Ciencias {student['Science Grade']}")
            print('\n')
    else:
        return print('Lista de estudiantes vacia')


def topThreeStudents(student_data):
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
        
        print(f"Top 3 de los estudiantes con mejor nota promedio:")
        for student in top_three:
            print(f"Nombre del estudiante:{student['Name']}\n")
    else:
        return print('Lista de estudiantes vacia')
    

def printAverageGrades(student_data):
    if student_data:
        for student in student_data:
            print(f"Nombre del Estudiante:{student['Name']}\nPromedio:{student['Average Grade']}")
    else:
        return print('Lista de estudiantes vacia')


def removeStudent(student_data):
    if student_data:
        counter=0
        index_to_be_removed= 0
        not_found=True
        student_name=is_valid_name('Digite el nombre del estudiante a eliminar ')
        student_section=is_valid_section('Digite la seccion del Estudiante ')
        for student in student_data:
            if student['Name'] == student_name and student['Section']== student_section:
                user_answer = is_valid_int(f"Seguro que desea eliminar a {student['Name']} de la seccion {student['Section']}? Digite:\n1. Para Sí\n2. Para No\n")
                if user_answer== 1:
                    index_to_be_removed=counter
                    student_data.pop(index_to_be_removed)
                    not_found=False
                    print(f'El estudiante {student_name} de la seccion {student_section} fue eliminado')
                    break
                elif user_answer==2:
                    not_found=False
                    break
                else:
                    print('Valor Ingresado no valido. Volviendo al menu...')
                    not_found=False
                    break
            counter+=1

        if not_found: 
                print(f'El estudiante {student_name} de la seccion {student_section} no existe')
    else:
        return print('Lista de estudiantes vacia')


def student_exists(student_name, student_section, students_list):
    if students_list:
        for student in students_list:
            if student['Name']==student_name and student['Section']== student_section:
                print(f"ERROR! El estudiante {student_name} de la seccion {student_section} ya existe. Ingrese uno nuevo \n")
                return True


def failed_student_list(students_list):
    if students_list:
        translator={'English Grade':'Nota de Ingles', 'Spanish Grade': 'Nota de Español', 'Socials Grade': 'Nota de Sociales', "Science Grade": 'Nota de Ciencias'}
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

                    
            for student in failed_students:
                        print(f"Nombre: {student['Name']}\nSeccion: {student['Section']}")
                        print('Materias Reprobadas:')
                        for subject, grade in student.items():
                            if subject=='Name' or subject=='Section' or subject=='Average Grade':
                                continue
                            else:
                                print(f"{translator[subject]}: {grade} ")
                        print('\n')
    else:
        return print('Lista de estudiantes vacia')

            



