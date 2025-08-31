class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next_node = next

class LinkedList:
    def __init__(self, root = None):
        self.root = root
        self.size = 0

    def add(self, data):
        node = Node(data, self.root)
        self.root = node
        self.size += 1

    def __repr__(self):
        next_n = self.root
        res = ""
        while next_n:
            res += str(next_n.data) + "->"
            next_n = next_n.next_node
        return res

    def remove(self, data):
        this_node = self.root
        prev_node = None
        while this_node:
            if this_node.data == data:
                if prev_node:
                    prev_node.next_node = this_node.next_node
                else:
                    self.root = this_node.next_node
                self.size -= 1
                return True     # removed the node with value data
            else:
                prev_node = this_node
                this_node = this_node.next_node
        return False            # did not find node with data


my_list = LinkedList()
my_list.add(5)
my_list.add(9)
my_list.add(7)
print(my_list)
print(my_list.remove(9))
print(my_list)
print(my_list.remove(9))

