def open_and_print_file_line_per_line(path):
    with open(path) as file:
        for line in file:
            print(f'Cancion: {line}')


def sorting_song_on_a_list(path):
    my_songs=[]
    with open(path) as file:
        for line in file:
            my_songs.append(line)
    my_songs.sort()
    return my_songs


def add_songs_to_new_file(old_path, new_path):
    my_song_list = sorting_song_on_a_list(old_path)
    with open(new_path, 'w', encoding='utf-8') as file:
        for song in my_song_list:
            file.write(song ) 
    open_and_print_file_line_per_line(new_path)


open_and_print_file_line_per_line('c:/Users/bjoseign/Desktop/LYFTER/Ejercicios de Manejo de Archivos/cancionex.txt')
add_songs_to_new_file('c:/Users/bjoseign/Desktop/LYFTER/Ejercicios de Manejo de Archivos/cancionesV2.txt', 'c:/Users/bjoseign/Desktop/LYFTER/Ejercicios de Manejo de Archivos/cancionex.txt')