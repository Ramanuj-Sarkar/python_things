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


# Calculates dividend / divisor
# where both dividend and divisor are base 10
# in the base of num_base
# to after_decimal places
# with digits separated by separator
# with negative-ness indicated by neg at the beginning
# separator can be used to clarify numbers in bases greater than 10
# dividend and divisor can only be ints
# outputs string which looks like float
def division_in_base(dividend: int, divisor: int, num_base=10, after_decimal=30, sep='', neg='-') -> str:
    if divisor == 0:
        raise ZeroDivisionError

    isNegative = (dividend < 0 or divisor < 0) and not (dividend < 0 and divisor < 0)

    abs_end = abs(dividend)
    abs_sor = abs(divisor)

    decimal = '.'

    # whole number component
    if abs_end < abs_sor:
        decimal = '0' + decimal
    else:
        # over_one is strictly the whole number
        over_one = abs_end // abs_sor
        while over_one > 0:
            decimal = str(over_one % num_base) + sep + decimal
            over_one //= num_base

    # new_dividend is strictly the remainder, which forms the decimal place
    new_dividend = abs_end % abs_sor

    if new_dividend == 0:
        decimal += "0"
    else:
        for x in range(after_decimal):
            if new_dividend == 0:
                break
            new_dividend *= num_base
            decimal += str(new_dividend // abs_sor) + sep
            new_dividend = new_dividend % abs_sor

    if(isNegative):
        return neg + decimal.rstrip(sep)
    else:
        return decimal.rstrip(sep)

    return decimal


division = False
integer = False

if __name__ == '__main__' and division:
    base = int(input("What base do you want to do this with?"))
    for x in range(-100, 100):
        if(x == 0):
            print(x, ': No.')
        else:
            print(x, ':', division_in_base(1, x, base))


if __name__ == '__main__' and integer:
    num_base = int(input("What base do you want?"))
    list_of_digits = make_digit_list(num_base)
    for x in range(-100,100):
        print(int_in_base_x_from_10(x,num_base,list_of_digits))
