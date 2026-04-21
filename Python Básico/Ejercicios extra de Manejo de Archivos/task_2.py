def reading_and_print(path):
    my_list=[]
    with open(path, encoding='utf-8') as file:
        for line in file:
            my_list+=line.split()
        return (len(my_list))

print(f'La cantidad de palabras es de {reading_and_print('c:/Users/bjoseign/Desktop/LYFTER/Ejercicios extra de Manejo de Archivos/textTask2.txt')}')



