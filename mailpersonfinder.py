import re


# Download Gmail files and find the person/people sending you the most mail
# filename indicates name of Gmail file
# start indicates the starting index (0 is who sends you the most mail, 1 is who sends you the second-most, etc
# span indicates how many people you want to see
def mail_finder(filename, start=0, span=10):
    all_people = {}

    with open(filename, 'r') as mail:
        not_trash = True
        for line in mail:
            if not_trash and len(line) >= 5 and line[:5] == 'From:':
                try:
                    values = re.search(r'<(.*)>$', line).group(1)
                    all_people[values] = all_people.get(values, 0) + 1
                except AttributeError:
                    all_people[line] = all_people.get(line, 0) + 1
            elif len(line) >= 14 and line[:15] == 'X-Gmail-Labels:':
                not_trash = 'Trash' not in line

    print(sorted(all_people.items(), key=lambda x: x[1], reverse=True)[start:start+span])
