def interleave_words_meanings(words_file, meanings_file, name):
    just_words = []
    with open(words_file, 'r') as f:
        just_words += f.read().split('\n')

    meanings = []
    with open(meanings_file, 'r') as f:
        meanings += f.read().split('\n')

    word_dict = {}
    base_word = just_words[0]
    for word in meanings:
        if word in just_words:
            base_word = word
            word_dict[base_word] = []
        else:
            word_dict[base_word].append(word)

    op = ('{|class="article-table sortable" style="text-align:center;"\n'
          '|+Dictionary\n'
          '|-\n'
          f'!{name} Orthography\n'
          '!English Words\n')
    for w in word_dict:
        op += f"|-\n|{w}\n|{',<br />'.join(word_dict[w])}\n"
    op += '|}'
    
    # to see it easily
    print(op)
    
    # to return it easily
    return op
