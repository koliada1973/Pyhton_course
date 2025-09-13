# Tree as class:
from idlelib.configdialog import changes

class Tree:
    def __init__(self, obj):
        self.data = obj
        self.left = None
        self.right = None

    def add_left(self, obj):
        if self.left is None:
            self.left = Tree(obj)
        else:
            temp = Tree(obj)
            temp.left =self.left
            self.left = temp

    def add_right(self, obj):
        if self.right is None:
            self.right = Tree(obj)
        else:
            temp = Tree(obj)
            temp.right = self.right
            self.right = temp

    def get_left(self):
            return self.left

    def get_right(self):
            return self.right

def show_tree(Node):
    if Node is None:
        return
    else:
        show_tree(Node.left)
        print(Node.data)
        show_tree(Node.right)




my_tree = Tree(100)
my_tree.add_left(50)
my_tree.add_right(150)
# print(f'Tree: \n{my_tree}')
#
my_tree.add_left(75)
my_tree.add_right(175)
print(f'Tree: \n{show_tree(my_tree)}')
# my_tree.show_tree(my_tree)
# print(my_tree.get_left())
# # # # print(my_tree.get_left().get_left())
# print(f'Tree: \n{my_tree}')
#
#
#
# my_tree2 = Tree(33)
# # print(my_tree2)
# my_tree2.add_left(22)
# # print(my_tree2)
# my_tree2.add_right(44)
# # print(my_tree2)
# # my_tree2.add_left(11)
# print(f'Tree: \n{my_tree2}')
#
# # my_tree.add_left(my_tree2)    # Не працює!!!
# # print(f'Tree: \n{my_tree}')






