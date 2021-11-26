def run_bf(code: str) -> None:
    pointer=0   # for instructions
    location=0  # for tape
    tape=[0]
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
            tape[location] += 1
        elif code[pointer] == '-':
            tape[location] -= 1
        elif code[pointer] == '.':
            print(chr(tape[location]),end='')
        elif code[pointer] == ',':
            tape[location] = ord(input())
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
