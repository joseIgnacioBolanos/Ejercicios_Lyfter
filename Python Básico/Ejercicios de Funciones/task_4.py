def reverse_word(my_word):
    reversed_word_result=''
    for letter in range(len(my_word)-1, -1, -1):
        reversed_word_result += (my_word[letter])
       
    return print(reversed_word_result)
    
    
def main():
    my_string = 'Me gustan los gatos'
    reverse_word(my_string)


main()