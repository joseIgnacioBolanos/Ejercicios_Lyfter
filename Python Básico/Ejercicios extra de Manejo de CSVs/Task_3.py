import csv

def reading_file(path_file):
    counting_genres={}
    with open(path_file, 'r', encoding='utf-8' ) as file:
        reader=csv.DictReader(file)
        for row in reader:
            if row['Genero'] in counting_genres:
                counting_genres[row['Genero']]+=1
            else:
                counting_genres[row['Genero']]=1
    return printing_genres(counting_genres)
    

def printing_genres(video_genres):
    sorted_genres= sorted(video_genres.keys())
    for item  in sorted_genres:
        print(f'{item} : {video_genres[item]}')
    
    


def main():
     reading_file('c:/Users/bjoseign/Desktop/LYFTER/Ejercicios extra de Manejo de CSVs/videoGames.csv')

main()