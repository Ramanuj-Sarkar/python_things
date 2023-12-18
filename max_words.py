# syllables is the number of possible syllables
# length is the maximum number of syllables in a word
def max_words(syllables,length):
    assert syllables >= 1, "There has to be at least 1 valid syllable."
    assert length >= 1, "Words have to be at least 1 syllable long."
    total = 0
    for x in range(1,length+1):
        total += syllables ** x
    print(total)


if __name__ == '__main__':
    max_words(1, 1)
