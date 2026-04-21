def searching_prime_numbers(my_list):
    prime_numbers_result=[]
    for number in my_list:
        if number ==2:
            prime_numbers_result.append(number)
        elif number % 2 == 0 or number ==1:
            continue
        else:
            is_prime=True
            for i in range(3, number):
                if number % i == 0:
                    is_prime=False
                    break
            if is_prime:
                prime_numbers_result.append(number)

    listing_prime_numbers_found(prime_numbers_result)


def listing_prime_numbers_found(prime_numbers_list):
    return print((prime_numbers_list))


def main():
    list_of_mixed_numbers=[1, 15, 21, 4, 6, 7, 13, 9, 67]
    searching_prime_numbers(list_of_mixed_numbers)


main()