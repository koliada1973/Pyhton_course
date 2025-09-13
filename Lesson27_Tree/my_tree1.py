class Tree:
    def __init__(self, obj, level=0):
        self.data = obj
        self.left = None
        self.right = None
        self.level = level

    def add_left(self, obj):
        if self.left is None:
            self.left = Tree(obj, self.level)
        else:
            temp = Tree(obj, self.left.level)
            self.left.level += 1
            temp.left = self.left
            self.left = temp
        self.left.level = self.level + 1

    def add_right(self, obj):
        if self.right is None:
            self.right = Tree(obj, self.level)
        else:
            temp = Tree(obj, self.right.level)
            self.right.level += 1
            temp.right = self.right
            self.right = temp
        self.right.level = self.level + 1

    def get_left_end(self, Node):
        if Node.left is None:
            return Node.left
        else:
            return self.get_left_end(Node.left)

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def __str__(self):
        res = '[Root:' + str(self.data) + '\n' + ' ' * (10 + 14 * self.level) + 'left=' + str(self.left) + '\n' + ' ' * (
                    10 + 14 * self.level) + 'right=' + str(self.right) + ']'
        return res






my_tree = Tree(100)

my_tree.add_left(50)
my_tree.add_right(150)
print(f'Tree: \n{my_tree}')

my_tree.add_left(75)
my_tree.add_right(175)


# show_tree(my_tree)

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