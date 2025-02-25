import re, string

def no_e_words():
    all_words = ''
    with open("words_alpha.txt", 'r') as words:
        all_words += words.read()

    words_list = all_words.split('\n')
    print(len(words_list))

    new_list = []
    for word in words_list:
        if 'e' not in word and len(word) > 3:
            new_list.append(word)

    print(len(new_list))

    print(new_list[:50])

    with open('words_without_e.txt', 'w') as new_words:
        new_words.write('\n'.join(new_list))

def tamoneh_words():
    all_words = ''
    with open("words_alpha.txt", 'r') as words:
        all_words += words.read()

    better_words = ' - '.join(all_words.split('\n —\n'))

    tamoneh = {}

    english = ['guide', 'people', 'will', 'prolly', 'look', 'the', 'here', 'too',
               'pin', 'this', 'who', 'ping', 'replied', 'to', 'your', 'europe', 'map', 'message',
               'asking', 'it', 'be', 'pinned', 'and', 'got', 'deleted', 'that', 'of', 'have', 'clue',
               'what', 'means', 'how', 'day', 'going', 'error', 'code', 'breaking', 'out', 'language',
               'can', 'explain', 'clearly', 'isnt', 'tone', 'tag', 'just', 'speaking', 'now', 'no', 'since',
               'understand', 'which']

    diaresis = ['ae', 'æ', 'aë', 'äe', 'aə', 'ei', 'ai', 'eï', 'eo', 'ew', 'eö', 'eu', 'eü',
                'ia', 'ja', 'iä', 'ie', 'ië', 'ïe', 'iə', 'io', 'jo', 'iö', 'iu', 'ju', 'iü',
                'oe', 'ɜ', 'oë', 'öe', 'oə', 'ou', 'u', 'oü', 'öu', 'ow', 'ua', 'wa', 'uä', 'ue',
                'we', 'uë', 'üe', 'uə', 'ui', 'wi', 'uï', 'uo', 'wo', 'uö', 'ə', 's', 'x', 'ŋ',
                'ng', 'ʝ', 'ï', 'ɮæ', 'ɣɤ', 'ʏ', 'ʒ', 'ə']

    for line in better_words.split('\n'):
        not_words = re.search("\d:\d\d [AP]M$", line)

        if not_words is None:
            wordlist = line.strip().lower().split(' ')
            for old_word in wordlist:
                word = re.sub(r'^[^\w\d]*|[^\w\d]*$', '', old_word)
                if word not in tamoneh:
                    tamoneh[word] = 0
                tamoneh[word] += 1

    sorted_tamoneh = sorted([(v, k) for k, v in tamoneh.items()], reverse=True)

    print(sorted_tamoneh)

    with open("simpler.txt", 'w') as words:
        words.write("")

    with open("simpler.txt", 'w+') as words:
        for w in sorted_tamoneh:
            words.write(w[1] + "\n")

def strumfari_words():
    all_words = ''
    with open("dumbtext.txt", 'r') as words:
        all_words += words.read()

    better_words = ' - '.join(all_words.split('\n —\n'))

    strumfari = {}

    english = []

    diaresis = []

    for line in better_words.split('\n'):
        not_words = re.search("\d:\d\d [AP]M$", line)

        if not_words is None:
            wordlist = line.strip().lower().split(' ')
            for old_word in wordlist:
                word = re.sub(r'^[^\w\d]*|[^\w\d]*$', '', old_word)
                if word not in strumfari:
                    strumfari[word] = 0
                strumfari[word] += 1

    sorted_strumfari = sorted([(v, k) for k, v in strumfari.items()], reverse=True)

    print(sorted_strumfari)
    print(len(sorted_strumfari))

    with open("simpler.txt", 'w') as words:
        words.write("")

    with open("simpler.txt", 'w+') as words:
        for w in sorted_strumfari:
            words.write(w[1] + "\n")



if __name__ == '__main__':
    tamoneh_words()
