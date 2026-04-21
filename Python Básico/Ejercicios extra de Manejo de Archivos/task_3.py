def reading_text(path):
    with open(path,  encoding='utf-8') as file:
        for line in file:
            print(line)

def capitalizing_words(path_with_no_capitals, path_with_capitals):
    
        try:
            with open(path_with_capitals, 'w', encoding='utf-8') as file_with_capitals:
                with open(path_with_no_capitals, encoding='utf-8') as file_with_no_capitals:
                    for line in file_with_no_capitals:
                        file_with_capitals.write(line.upper())
            reading_text(path_with_capitals)
        except FileNotFoundError as e:
            print(e)
        except PermissionError as e:
            print(e)
        
            




reading_text('c:/Users/bjoseign/Desktop/LYFTER/Ejercicios extra de Manejo de Archivos/textTask3.txt')
capitalizing_words('c:/Users/bjoseign/Desktop/LYFTER/Ejercicios extra de Manejo de Archivos/textTask3.txt', 'c:/Users/bjoseign/Desktop/LYFTER/Ejercicios extra de Manejo de Archivos/textTask3V2.txt')
