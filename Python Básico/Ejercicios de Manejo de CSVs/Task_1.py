import csv
def crating_dictionaries(number_of_games):
    video_game=[]
    name=''
    genre=''
    developer=''
    classification = ''
    for i in range(number_of_games):
        name= input('Nombre ')
        genre=input('Genero ')
        developer=input('Desarrollador ')
        classification = input('Clasificación ESRB ')

        game={
            'Nombre': name,
            'Genero': genre,
            'Desarrollador': developer,
            'Clasificación ESRB': classification
        }
        video_game.append(game)


    return(video_game)



def write_csv_file(file_path, data, headers):
    with open(file_path, 'w', newline='',encoding='utf-8') as file:
        writer= csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(data)
    return read_cvs_file(file_path)

def read_cvs_file(file_path):
    with open(file_path,'r',encoding='utf-8' ) as file:
        reader= csv.DictReader(file)
        for row in reader:
            print(row)
    

def main():
    try:
        n = int(input('Ingrese la cantidade de video juegos que desea ingresar: '))
        my_video_game= crating_dictionaries(n)
        write_csv_file('c:/Users/bjoseign/Desktop/LYFTER/Ejercicios de Manejo de CSVs/videoGames.csv', my_video_game , my_video_game[0].keys())
    except ValueError as e:
        print(e)
main()