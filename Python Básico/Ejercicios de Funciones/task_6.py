def ordering_alphabetically(user_string):
    temp = ''
    my_list=[]
    for char in user_string:
        if char != '-':
            temp+=char
        elif char == '-':
                if temp=='' :
                    continue
                else:
                    my_list.append(temp)
                    temp = ''

    if temp  != '':
        my_list.append(temp)
            

    my_list.sort()
   
    arrange_result = ''
    for word in range(0,len(my_list)):
        arrange_result += my_list[word] 
        if word != len(my_list)-1:
            arrange_result+='-'

    return print(arrange_result)


def main():
    my_string= 'python-variable-funcion-computadora-monitor'
    ordering_alphabetically(my_string)

main()
        