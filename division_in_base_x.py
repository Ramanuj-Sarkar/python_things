#Calculates dividend / divisor
#in the base of base_number
#to after_decimal places
#with digits separated by separator
#separator can be used to clarify numbers in bases greater than 10
#dividend and divisor can only be ints
#outputs string which looks like float
def division_in_base(dividend : int, divisor : int, base_number = 10, after_decimal = 30, separator = '') -> str:
    if divisor == 0:
        raise ZeroDivisionError

    decimal = '.'
    
    #whole number component
    if dividend < divisor:
        decimal = '0' + decimal
    else:
        #over_one is strictly the whole number
        over_one = dividend // divisor
        while over_one > 0:
            decimal = str(over_one % base_number) + separator + decimal
            over_one //= base_number
    
    #new_dividend is strictly the remainder, which forms the decimal place
    new_dividend = dividend % divisor

    if new_dividend == 0:
        decimal += "0"
    else:
        for x in range(after_decimal):
            if new_dividend == 0:
                break
            new_dividend *= base_number
            decimal += str(new_dividend // divisor) + separator
            new_dividend = new_dividend % divisor

    return decimal

if __name__ == '__main__':
    #prints all numbers from 1/1 to 1/30 in base six, with at most 50 digits after the decimal place
    for x in range(1,31):
        print(x, ':', division_in_base(1,x,6,50))
