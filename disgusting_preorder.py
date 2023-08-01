# This exists so I could represent a linear string as a tree
# and represent a tree as a linear string
# in terms of which order the characters would be seen.
# It is disgusting, especially make_preorder.

linear_number = 0

# This takes a linear string
# and turns it into a tree which would be read
# the same way as the linear string using pre-order.
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

# This takes in a string representing the tree
# and reads it using pre-order
# thereby resurrecting the original string.
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
