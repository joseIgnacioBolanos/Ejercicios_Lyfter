def counting_uppercase_and_lowercase(my_word):
    uppercase_counter = 0
    lowercase_counter=  0
    for char in my_word:
        if char.isupper():
            uppercase_counter+= 1
        elif char.islower():
            lowercase_counter+=1
    print(f'El numero de letras mayusculas {uppercase_counter} y el numero de letras minusculas es de {lowercase_counter}')


def main():
    my_string= 'I love Nación Sushi'

    counting_uppercase_and_lowercase(my_string)

main()