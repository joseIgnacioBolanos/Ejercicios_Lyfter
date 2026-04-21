def counting_letters(user_words, user_number):
    my_new_list=[]
    for word in user_words:
        counter=0
        for char in word:
            counter+=1

        if counter > user_number:
            my_new_list.append(word)

    return print(my_new_list)


def main():
    list_of_words= ["cielo", "sol", "maravilloso", "día"]
    number_letters_to_find = int(input('Ingrese el numero de letras minimas en la palabra: '))


    counting_letters(list_of_words, number_letters_to_find)

main()