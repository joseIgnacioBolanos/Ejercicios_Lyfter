import action, data 

def menu():
    students_list=[]
    while True:
        user_option= action.is_valid_int('\nEnter:\n1. To add a new student\n2. To view the list of students\n3. To view the top 3 students with the highest average grades\n4. To view the average note of all students.\n5. To remove a student\n6. To view the list of failed students\n7. To export the data to a CSV file.\n8. To import the CSV data previously exported.\n9. Exit\n')
        if user_option == 1:
            action.adding_student_data(students_list)
        elif user_option == 2:
            action.print_student_data(students_list)
        elif user_option == 3:
            action.top_three_students(students_list)
        elif user_option == 4:
            action.print_average_grades(students_list)
        elif user_option == 5:
            action.remove_student(students_list)
        elif user_option == 6:
            action.failed_student_list(students_list)
        elif user_option == 7:
            data.save_students("my_students_list.csv", students_list)
        elif user_option == 8:
            students_list= data.import_students_data('my_students_list.csv')  
        elif user_option == 9:
            print('Closing..')
            break
                 
        else:
            print('Invalid input value')
        
            
