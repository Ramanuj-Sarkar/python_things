import re


def danicb_encoder(query_string):
    assert sum(1 for x in query_string if ord('a') > ord(x) or ord('z') < ord(x)) == 0, "A valid text contains only" \
                                                                                  "lowercase letters between a and z."
    output = ''
    # turns wimpmode text into required danicb input
    for char in query_string:
        letter = ord(char) - 97
        output += 'f' * (1 + letter // 5)
        output += " "
        if letter < 25:
            # not z
            output += 'f' * (1 + letter % 5)
            output += " "
    return output.rstrip(' ')


def danicb_decoder(query_string):
    assert sum(1 for x in query_string if x != 'f' and x != ' ') == 0, "A valid input contains only 'f' and ' '."
    output = ''
    # turns required danicb input text into wimpmode text
    regex_output = re.findall(r"(?:f{1,5} f{1,5})|f{6}", query_string)
    for letter in regex_output:
        check = letter.split(' ')
        if len(check) == 1:
            # f{6}
            output += 'z'
        else:
            fives = len(check[0]) - 1
            ones = len(check[1]) - 1
            output += chr(fives * 5 + ones + 97)
    return output


if __name__ == '__main__':
    queries = ['thequickbrownfoxjumpedoverthelazydog',
               'abcdefghijklmnopqrstuvwxyz',
               'printtartstcaphellocomspacecapworldexctsttar',
               'readtarargtarprinttarargtar'
               ]
    for query in queries:
        encoded = danicb_encoder(query)
        print(encoded)
        decoded = danicb_decoder(encoded)
        print(decoded)
        print()
