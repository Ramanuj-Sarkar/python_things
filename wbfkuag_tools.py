# These tools allow you to encrypt and decrypt text
# in a cipher that I often use.

def wbfkuag_maker(total):
    string = 'qwertyuiopasdfghjklzxcvbnm'
    shifted = string[1:] + string[0]

    string, shifted = string + string.upper(), shifted + shifted.upper()

    zipped = {a: b for a, b in zip(shifted, string)}
    return ''.join(zipped[x] if x in zipped else x for x in total)

def wbfkuag_translator(total):
    string = 'qwertyuiopasdfghjklzxcvbnm'
    shifted = string[1:] + string[0]

    string, shifted = string + string.upper(), shifted + shifted.upper()

    zipped = {a: b for a, b in zip(string, shifted)}
    return ''.join(zipped[x] if x in zipped else x for x in total)
