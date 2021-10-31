# takes in number
# returns a list of groupings
# of coin flips which can be used
# to find a digit in range(0,number)
# if the coin flips are modeled as positive binary digits
def binary_coin_flip(numbers: int):
    grouped_coins = []
    while numbers != 0:
        coins = 1
        while ((2 ** (coins + 1)) - 1) <= numbers:
            coins += 1
        numbers -= (2 ** coins) - 1
        grouped_coins.append(coins)
    return grouped_coins
