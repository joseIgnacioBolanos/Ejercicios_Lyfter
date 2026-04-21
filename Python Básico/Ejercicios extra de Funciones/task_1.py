def counting_words(text, letter):
    counter = 0
    for char in text:
        if char == letter:
            counter+= 1
    return print(f"Se a encontrado {counter} veces el carácter ")


def main():
    my_sentence='programacionO'
    my_sentence_lower= my_sentence.lower()
    letter_to_find= input('Ingrese el carácter que desea buscar ')
    letter_to_find_lower= letter_to_find.lower()
    counting_words(my_sentence_lower, letter_to_find_lower)


main()
