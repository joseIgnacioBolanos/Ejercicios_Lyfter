def printing_file(path):
    with open(path, encoding='utf-8') as file:
        for line in file:
            print(line)


def adding_sting_to_file(new_sting,  path):
    with open(path, 'a', encoding='utf-8') as file:
        file.write(new_sting)
    printing_file(path)


def main():
        while True:
            my_sting= input('Digite una linea de texto ')
            if my_sting.strip() == '':
                print('Debes digitar un texto')
            else:
                adding_sting_to_file(my_sting, 'c:/Users/bjoseign/Desktop/LYFTER/Ejercicios extra de Manejo de Archivos/miFrase.txt')

    
main() 
