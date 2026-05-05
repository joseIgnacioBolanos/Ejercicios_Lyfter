import action, data 

def menu():
    students_list=[]
    while True:
        userOption= action.is_valid_int('\nDigite:\n1. Para agregar Información de Estudiantes\n2. Para ver la lista de Estudiantes\n3. Para ver el top 3 de los estudiantes con la mejor nota promedio\n4. Para ver la nota promedio de todos los estudiantes\n5. Para eliminar un Estudiante\n6. Para ver los estudiantes reprobados\n7. Exportar todos los datos actuales a un archivo CSV.\n8. Para importar los datos de un archivo CSV previamente exportado.\n')
        if userOption == 1:
            action.addingStudentData(students_list)
        elif userOption == 2:
            action.printStudentData(students_list)
        elif userOption == 3:
            action.topThreeStudents(students_list)
        elif userOption == 4:
            action.printAverageGrades(students_list)
        elif userOption == 5:
            action.removeStudent(students_list)
        elif userOption == 6:
            action.failed_student_list(students_list)
        elif userOption == 7:
            data.save_students("my_students_list.csv", students_list)
        elif userOption == 8:
            data.read_students_data('my_students_list.csv')           
        else:
            print('Valor ingresado inválido')
        
                

menu() 
