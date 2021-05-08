def base_shift(base):
    base_dict = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'T'}

    return base_dict[base] if base in base_dict else base


def other_strand(template_strand):
    return ''.join(base_shift(x) for x in template_strand)


def double_stranded_dna(template_strand):
    return f"{template_strand} input strand\n" \
           f"{other_strand(template_strand)} corresponding strand"


if __name__ == '__main__':
    template = input('Please input the DNA strand here:  ')
    print('The corresponding strand would be:', other_strand(template))
    print('Here are the two side-by-side:')
    print(double_stranded_dna(template))
