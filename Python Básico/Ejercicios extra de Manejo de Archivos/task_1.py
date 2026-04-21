def reading_and_print(path):
    with open(path) as file:
        for line in file:
            print(line)

def removing_line_break(path):
    my_list=[]
    with open(path) as file:
        for line in file:
            my_list.append(line.strip())
    return my_list


def creating_new_file(old_path, new_path):
    list_of_words= removing_line_break(old_path)
    with open(new_path, 'w', encoding='utf-8') as file:
        for line in list_of_words:
            file.write(line + ' ')
    reading_and_print(new_path)
        


def main():
    try:

        reading_and_print('c:/Users/bjoseign/Desktop/LYFTER/Ejercicios extra de Manejo de Archivos/miFrase.txt')
        creating_new_file('c:/Users/bjoseign/Desktop/LYFTER/Ejercicios extra de Manejo de Archivos/miFrase.txt', 'c:/Users/bjoseign/Desktop/LYFTER/Ejercicios extra de Manejo de Archivos/miBoots.txt')
    except FileNotFoundError as e:
        print(e)

main()