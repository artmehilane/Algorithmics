def insert(tree, value):
    if tree is None:
        tree = [value, None, None]
    else:
        root_value = tree[0]
        if value < root_value:
            tree[1] = insert(tree[1], value)
        else:
            tree[2] = insert(tree[2], value)

    return tree

def inorder(tree):
    if tree is not None:
        inorder(tree[1])
        print(tree[0], end = ' ')
        inorder(tree[2])



tree = None

for value in [2, 6, 4, 3, 1, 7, 5]:
    tree = insert(tree, value)

#Prindi puu kasvavas järjestuses

inorder(tree)

