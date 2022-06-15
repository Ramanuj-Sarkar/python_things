def balanced_to_unbalanced_ternary(number) -> str:
    backwards_number = str(number)[::-1].rstrip('0')
    assert set(backwards_number).issubset({'0','1','2'}),\
        'This number should contain only the characters 0, 1, or 2.'

    if backwards_number == '':
        return '0'

    len_backwards_number = len(backwards_number)
    added_number = [0] * (len_backwards_number + 1)

    for digit in range(len_backwards_number):
        added_digit = int(backwards_number[digit]) + 1
        added_number[digit] += added_digit
        if added_number[digit] > 2:
            added_number[digit] = added_number[digit] % 3
            added_number[digit + 1] += 1

    final_number = [''] * (len_backwards_number + 1)
    digit_change_dict = {0: 'T', 1: '0', 2: '1'}
    for num, digit in enumerate(added_number):
        final_number[num] = (digit_change_dict[digit] if num < len_backwards_number else str(digit))
    return ''.join(final_number)[::-1].lstrip('0')


if __name__ == "__main__":
    times = 0
    maximum = int(input('Enter an integer:'))
    balanced_ternary_value = [0]
    while times < maximum:
        digit = 0
        balanced_ternary_value[digit] += 1
        while balanced_ternary_value[digit] == 3:
            balanced_ternary_value[digit] = 0
            digit += 1
            if digit == len(balanced_ternary_value):
                balanced_ternary_value.append(0)
            balanced_ternary_value[digit] += 1
        print(times, balanced_to_unbalanced_ternary(''.join([str(x) for x in balanced_ternary_value[::-1]])))
        times += 1
