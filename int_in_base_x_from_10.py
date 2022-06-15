# Makes a list of string digits for the int_in_base_x_from_10 function
def make_digit_list(length : int):
    digit_list = []

    # This for-loop enters the digits which are used to represent the base.
    # 0-9 are normal Arabic numerals.
    # Numbers larger than 9 are decided by user choice.
    for x in range(length):
        if x < 10:
            digit_list.append(str(x))
        else:
            digit_list.append(input('Write a digit to represent {}:'.format(x)))

    return digit_list


# Outputs a string representing a num
# in base base
# with the digits in digit_list
# separated by sep
# with negative-ness indicated by neg at the beginning
def int_in_base_x_from_10(num : int, base=10, digit_list=[], sep="", neg = "-"):
    # This if-statement allows the bases to be higher than 10.
    if len(digit_list) == 0:
        digit_list = make_digit_list(base)

    # This elif-statement stops people from having digit lists which are too small.
    elif len(digit_list) < base:
        return 'Please double-check the length of your digit list.'

    if(num == 0):
        return digit_list[0]

    temp_num = abs(num)
    answer = ""

    # This while loop constructs the answer
    # by getting the remainders
    # which exist in the base
    # until the number is 0.
    while temp_num > 0:
        answer = digit_list[temp_num % base] + sep + answer
        temp_num //= base

    if(num < 0):
        return neg + answer.rstrip(sep)
    else:
        return answer.rstrip(sep)


if __name__ == '__main__':
    num_base = int(input("What base do you want?"))
    list_of_digits = make_digit_list(num_base)
    for x in range(-100,100):
        print(int_in_base_x_from_10(x,num_base,list_of_digits))
