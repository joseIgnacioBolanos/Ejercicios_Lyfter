import csv

def printing_csv_file(file_path):
    finder=False
    with open(file_path, 'r', encoding='utf-8') as file:
        reader=csv.DictReader(file)
        developer_name=input('Digite el nombre del desarrollador:')
        for row in reader:
            if row['Desarrollador'] == developer_name and finder==False:
                print(f"Video Juegos desarrollados por {developer_name}:\n- {row['Nombre']} ( Clasificacion: {row['Clasificación ESRB']} Genero: {row['Genero']}) " )
                finder=True
            else:
                if row['Desarrollador'] == developer_name:
                    print(f"- { row['Nombre']} ( Clasificacion: {row['Clasificación ESRB']} Genero: {row['Genero']})")

        if finder == False:
            print(f'No se encontró un video juego del desarrollador {developer_name}')


def main():
     printing_csv_file('c:/Users/bjoseign/Desktop/LYFTER/Ejercicios extra de Manejo de CSVs/videoGames.csv')

main()