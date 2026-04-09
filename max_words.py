# syllables is the number of possible syllables
# length is the maximum number of syllables in a word
def max_words(syllables,length):
    if syllables < 1:
        raise ValueError("There has to be at least 1 valid syllable.")
    if length < 1:
        raise ValueError("Words have to be at least 1 syllable long.")
    return sum(syllables ** x for x in range(1,length+1))


if __name__ == '__main__':
    max_words(1, 1)
