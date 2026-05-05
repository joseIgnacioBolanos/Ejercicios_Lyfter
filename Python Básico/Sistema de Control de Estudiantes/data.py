import csv

def save_students(file_path, data):
    
    with open(file_path, 'w', encoding='utf-8', newline='') as file:

        headers = data[0].keys()

        writer = csv.DictWriter(file, fieldnames=headers)

        writer.writeheader()

        writer.writerows(data)



def read_students_data(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for student in reader:
                print(f"Nombre: {student['Name']}\nSeccion: {student['Section']}\nNota De Ingles: {student['English Grade']}\nNota de Español: {student['Spanish Grade']}\nNota de Sociales {student['Socials Grade']}\nNota de Ciencias: {student['Science Grade']}")
    except FileNotFoundError:
        print('Aun no existe el archivo que deseas abrir')

