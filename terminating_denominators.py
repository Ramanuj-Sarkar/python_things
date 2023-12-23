from math import floor, log2

# returns a list of all numbers which can be represented as 2^x where x is an integer
# as long as they are less than and not equal to maximum
# the denominators would form terminating decimals in binary if translated
# the list is in order without duplicates
def terminating_binary_denominators(maximum: int) -> list:
    return [2 ** i for i in range(floor(log2(maximum)))]


# returns a list of all numbers which can be represented as 2^x * 3^y where x and y are integers
# as long as they are less than and not equal to maximum
# the denominators would form terminating decimals in senary if translated
# the list is in order without duplicates
def terminating_senary_denominators(maximum: int) -> list:
    mutated_set = {1}
    ordered_list = []

    min_mut = min(mutated_set)
    while min_mut < maximum:
        mutated_set |= {min_mut * 2, min_mut * 3}
        ordered_list.append(min_mut)
        mutated_set.remove(min_mut)
        min_mut = min(mutated_set)

    return ordered_list


if __name__ == '__main__':
    value = 10000000

    print(len(terminating_binary_denominators(value)))

    print(len(terminating_senary_denominators(value)))
