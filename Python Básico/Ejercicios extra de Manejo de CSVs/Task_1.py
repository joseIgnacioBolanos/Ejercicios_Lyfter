import csv

def reading_file_csv(file_path):
    counter= 0
    list_of_headers=[]
    with open(file_path, 'r', encoding= 'utf-8') as file:
        reader=csv.reader(file)
        for row in reader:
                if counter==0:
                    for index in range(0, len(row)):
                        list_of_headers.append(row[index])
                    counter+=1
                    continue
                else:
                    for i in range(0, len(row)):
                        print(f'{list_of_headers[i]}: {row[i]}')
                    print('\n')

            
def main():
    reading_file_csv('c:/Users/bjoseign/Desktop/LYFTER/Ejercicios de Manejo de CSVs/videoGames.csv')


main()