linear_number = 0

def make_preorder(linear, treeshape=[''], treeshape_number=1):
    if treeshape == ['']:
        treeshape = [''] * len(linear)
    global linear_number
    treeshape[treeshape_number-1] = linear[linear_number]
    if treeshape_number * 2 <= len(linear):
        # if input() != '': return
        linear_number += 1
        make_preorder(linear, treeshape, treeshape_number * 2)
    if treeshape_number * 2 + 1 <= len(linear):
        # if input() != '': return
        linear_number += 1
        make_preorder(linear, treeshape, treeshape_number * 2 + 1)
    return ''.join(treeshape)

def decode_preorder(treestring, treestring_number=1):
    output_string = treestring[treestring_number-1]
    if treestring_number * 2 <= len(treestring):
        # if input() != '': return
        output_string += decode_preorder(treestring, treestring_number * 2)
    if treestring_number * 2 + 1 <= len(treestring):
        # if input() != '': return
        output_string += decode_preorder(treestring, treestring_number * 2 + 1)
    return output_string

ultimate_machine = 'ABCDEFGHIJKLMNOP'

linear_number = 0

for maxo in range(1,len(ultimate_machine)+1):
    linear_number = 0
    truth_machine = ultimate_machine[:maxo]
    things = [''] * maxo
    preodered_string = make_preorder(truth_machine)
    print(preodered_string)
    print(decode_preorder(preodered_string))

linear_number = 0
print()
code = '++++++[<++++++++^>++++++++^-],<[-^-<]^[-[<>-^]>+[.]]>[.^]'
trench = [''] * len(code)
finished = make_preorder(code)
print(finished)
print(decode_preorder(finished))
