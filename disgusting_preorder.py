# The preorder used to be worse, requiring a global variable.
# It no longer requires that, but it is still a little disgusting, isn't it?

# This takes a linear string
# and turns it into the linear representation of
# a tree which would be read the same way as the linear string using pre-order.
def make_preorder(linear, linear_num=0, tree_num=1, final=True):
    starting_num = linear_num
    tree_correlations = {tree_num: linear[linear_num]}
    if tree_num * 2 <= len(linear):
        starting_num += 1
        temp, more_correlations = make_preorder(linear, starting_num, tree_num * 2, False)
        starting_num += temp
        tree_correlations |= more_correlations
    if tree_num * 2 + 1 <= len(linear):
        starting_num += 1
        temp, more_correlations = make_preorder(linear, starting_num, tree_num * 2 + 1, False)
        starting_num += temp
        tree_correlations |= more_correlations

    if final:
        return ''.join([string for _, string in sorted(tree_correlations.items())])
    else:
        return starting_num - linear_num, tree_correlations


# This takes in a string representing a tree
# and reads it using pre-order
# thereby resurrecting the original string.
def decode_preorder(tree_string, tree_number=1):
    output_string = tree_string[tree_number-1]
    if tree_number * 2 <= len(tree_string):
        output_string += decode_preorder(tree_string, tree_number * 2)
    if tree_number * 2 + 1 <= len(tree_string):
        output_string += decode_preorder(tree_string, tree_number * 2 + 1)
    return output_string
