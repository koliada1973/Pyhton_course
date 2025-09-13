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

def preorder(root):
    if root is not None:
        print(root.root)
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root is not None:
        preorder(root.left)
        preorder(root.right)
        print(root.root)

def inorder(root):
    if root is not None:
        preorder(root.left)
        print(root.root)
        preorder(root.right)

def printexp(tree):
  sVal = ""
  if tree:
      sVal = '(' + printexp(tree.get_left())
      sVal = sVal + str(tree.root)
      sVal = sVal + printexp(tree.get_right())+')'
  return sVal

my_tree = Tree(100)
my_tree.add_left(50)
my_tree.add_right(150)
my_tree.add_left(75)
my_tree.add_right(175)


my_tree.get_left().add_right(51)
my_tree.get_right().add_left(149)

# print(my_tree.get_left())
# print(my_tree.get_left().get_left())
# print(my_tree)

preorder(my_tree)
print()
postorder(my_tree)
print()
inorder(my_tree)

print(printexp(my_tree))
