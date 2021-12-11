ef run_bf(code: str) -> None:
    pointer = 0     # for instructions
    location = 0    # for tape
    tape = [0]
    input_string = chr(10)  # allows multiple inputs to happen easily

    # checks balance
    balance = 0
    for char in code:
        if char == '[':
            balance += 1
        elif char == ']':
            balance -= 1
        assert balance >= 0, 'unmatched ]'
    assert balance == 0, 'unmatched ['

    while pointer < len(code):
        if code[pointer] == '>':
            location += 1
            if location == len(tape):
                tape.append(0)
        elif code[pointer] == '<':
            location -= 1
            if location < 0:
                tape = [0] + tape
                location += 1
        elif code[pointer] == '+':
            tape[location] = (tape[location] + 1) % 256
        elif code[pointer] == '-':
            tape[location] = (tape[location] - 1) % 256
        elif code[pointer] == '.':
            print(chr(tape[location]),end='')
        elif code[pointer] == ',':
            if input_string == chr(10):
                input_string = input(">>") + chr(10)
            if len(input_string) > 0 and ord(input_string[0]) != chr(10):
                tape[location] = ord(input_string[0])
            input_string = input_string[1:]
        elif code[pointer] == '[':
            if tape[location] == 0:
                nest_counter = 0
                while code[pointer] != ']' or nest_counter >= 0:
                    pointer += 1
                    if code[pointer] == '[':
                        nest_counter += 1
                    elif code[pointer] == ']':
                        nest_counter -= 1
        elif code[pointer] == ']':
            if tape[location] != 0:
                nest_counter = 0
                while code[pointer] != '[' or nest_counter >= 0:
                    pointer -= 1
                    if code[pointer] == ']':
                        nest_counter += 1
                    elif code[pointer] == '[':
                        nest_counter -= 1
        pointer += 1
