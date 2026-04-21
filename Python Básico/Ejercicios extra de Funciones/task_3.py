def counting_vocals(user_word):
    counter= 0
    for char in user_word:
        if char == 'a' or char == 'e' or char == 'i' or char ==  'u' or char == 'o':
            counter+=1

    return(print(counter))

def main():
    my_sentence= 'Hola mundO'
    my_sentence_lower= my_sentence.lower()
    counting_vocals(my_sentence_lower)

main()