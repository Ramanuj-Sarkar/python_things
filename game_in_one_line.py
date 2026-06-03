print("You pass!" if not [print(f"Incorrect; the number is {digit}") for count, digit in zip(["2+2", "3+5"], ["4", "8"]) if digit != input(f"Type the answer to {count}:")] else "You lose...")
