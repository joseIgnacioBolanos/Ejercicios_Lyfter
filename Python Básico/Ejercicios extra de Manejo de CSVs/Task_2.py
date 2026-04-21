import csv

def reading_csv_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader= csv.DictReader(file)
        finder=False
        user_option=input('Digite la clasificacion que deseas buscar: ')
        for row in reader:
                if row['Clasificación ESRB'] == user_option and finder==False:
                    print(f"Video Juegos con la clasificación {user_option}:\n- {row['Nombre']} ( Clasificacion: {row['Clasificación ESRB']}, Genero: {row['Genero']}) " )
                    finder=True
                else:
                    if row['Clasificación ESRB'] == user_option:
                         print(f"- { row['Nombre']} ( Clasificacion: {row['Clasificación ESRB']}, Genero: {row['Genero']})")
        if finder == False:
             print(f'Lo sentimos! \nEl video juego con la clasificacion {user_option} no existe')
             
def main():
     reading_csv_file('c:/Users/bjoseign/Desktop/LYFTER/Ejercicios extra de Manejo de CSVs/videoGames.csv')

main()