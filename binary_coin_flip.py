# With n coins, you can add a number from 0 to 2^n - 1.
def binary_coin_flip(numbers: int):
    grouped_coins = []
    assert numbers >= 0, 'A negative number is not a valid input.'
    while numbers != 0:
        coins = 1
        while ((2 ** (coins + 1)) - 1) <= numbers:
            coins += 1
        numbers -= (2 ** coins) - 1
        grouped_coins.append(coins)
    return grouped_coins


if __name__ == "__main__":
    num = int(input('Enter a number:'))
    print(binary_coin_flip(num))
    print("Using binary numbers, you get: ")
    coins_dict = dict()
    for x in range(num):
        coins = sum(binary_coin_flip(x))
        if coins not in coins_dict:
            coins_dict[coins] = set()
        coins_dict[coins].add(x)

    for coins_used in coins_dict:
        print(f"Use {coins_used} numbers: {coins_dict[coins_used]}")
