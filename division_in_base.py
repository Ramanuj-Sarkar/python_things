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


if __name__ == '__main__':
    base = int(input("What base do you want to do this with?"))
    for x in range(-100, 100):
        if(x == 0):
            print(x, ': No.')
        else:
            print(x, ':', division_in_base(1, x, base))
