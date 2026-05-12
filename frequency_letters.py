def frequency_letters(letters):
    spletters = letters.split('\n')

    old_frequencies = sorted([x[:-1].split(' / ') for x in spletters], key=lambda x: -float(x[1]))

    new_frequencies = [x for x in zip((x[0] for x in old_frequencies[::-1]), (float(x[1]) for x in old_frequencies))]

    return new_frequencies


if __name__ == '__main__':

    consonants = '''n / 7.11%
r / 6.94%
t / 6.91%
s / 4.75%
d / 4.21%
l / 3.96%
k / 3.18%
ð / 2.95%
m / 2.76%
z / 2.76%
p / 2.15%
v / 2.01%
w / 3.79%
b / 1.80%
f / 1.71%
h / 1.40%
ŋ / 0.99%
ʃ / 0.97%
j / 4.31%
g / 0.80%
dʒ / 0.59%
tʃ / 0.56%
θ / 0.41%
ʒ / 0.07%'''

    vowels = '''ʌ / 13.855%
ɪ / 8.125%
ɛ / 3.755%
æ / 2.35%
ɑ / 3.43%
ʊ / 1.395%'''

    clist = frequency_letters(consonants)
    vlist = frequency_letters(vowels)

    print(clist, "\n", vlist)
