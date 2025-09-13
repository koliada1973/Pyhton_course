# Tree as list:

def create_tree(r):
    return [r, [], []]

def insert_left(tree, node):
    temp = tree.pop(1)
    if len(temp) > 0:
        tree.insert(1, [node, temp, []])
    else:
        tree.insert(1, [node, [], []])

def insert_right(tree, node):
    temp = tree.pop(2)
    if len(temp) > 0:
        tree.insert(2, [node, temp, []])
    else:
        tree.insert(2, [node, [], []])

def get_left(tree):
    return tree[1]

def get_right(tree):
    return tree[2]

t = create_tree(5)
insert_left(t, 3)
insert_left(t, 4)
print(t)
b3 = get_left(get_left(t))
insert_left(b3, 1)
insert_right(b3, 2)
insert_right(t, 10)
print(t)