class Tree:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None

    def add_left(self,data):
        if self.left is None:
            self.left = Tree(data)

        else:
            temperory_left = Tree(data)
            temperory_left.left = self.left
            self.left = temperory_left

    def add_right(self,data):
        if self.right is None:
            self.right = Tree(data)

        else:
            temperory_right = Tree(data)
            temperory_right.right = self.right
            self.right = temperory_right

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def __str__(self):
        return str(self.root)


my_tree = Tree(100)
my_tree.add_left(50)
my_tree.add_right(150)
my_tree.add_left(75)
my_tree.add_right(175)
# print(my_tree)
# print(my_tree.root,my_tree.left.root,my_tree.left.left.root,my_tree.right.root)

print(my_tree.get_left())
print(my_tree.get_left().get_left())
print(my_tree)