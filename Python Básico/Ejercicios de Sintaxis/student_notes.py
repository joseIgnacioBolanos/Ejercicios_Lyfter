total_notes = int(input("Ingrese la cantidad de notas"))
notes_counter = 1
approved_notes= 0
failed_notes = 0
average_notes_approved = 0
average_notes_failed= 0
average_total_notes=0

while notes_counter <= total_notes:
    current_note= int(input(f"Ingrese la nota numero {notes_counter} "))
    if current_note < 70:
        failed_notes = failed_notes +1 
        average_notes_failed = average_notes_failed + current_note
        notes_counter= notes_counter+1
    else:
        approved_notes = approved_notes +1
        average_notes_approved = average_notes_approved + current_note
        notes_counter= notes_counter+1
    average_total_notes= average_total_notes+(current_note / total_notes)


if (failed_notes == 0):
    average_notes_failed =0
else:
    average_notes_failed = average_notes_failed / failed_notes

if (approved_notes == 0):
    average_notes_approved =0
else:
    average_notes_approved = average_notes_approved / approved_notes

print(f"El estudiante tiene esta cantidad de notas aprobadas {approved_notes}")
print(f"Este es el promedio de notas aprobadas {average_notes_approved}")
print(f"El estudiante tiene esta cantidad de notas desaprobadas {failed_notes}")
print(f"Este es el promedio de notas desaprobadas {average_notes_failed}")
print(f"Este es el promedio de total de notas {average_total_notes} ")





