class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def add(self, item):
        if self.head == None:
            self.head = Node(item)
        else:
            temp = Node(item)
            temp.next = self.head
            self.head = temp

    def __str__(self):
        result = ""
        current = self.head
        while current:
            result += str(current.value) + ' > '
            current = current.next
        return result

    def search(self, value):
        temp = self.head
        while temp:
            if temp.value == value:
                return True
            temp = temp.next
        return False

    def search_all(self, value):
        temp = self.head
        index = 0
        a = list()
        while temp:
            if temp.value == value:
                a.append((index, temp.value))
            temp = temp.next
            index += 1
        return a

    def remove(self, value):
        temp = self.head
        prev = None
        if value == self.head.value:
            self.head = self.head.next
        else:
            while temp:
                if temp.value == value:
                    prev.next = temp.next
                    break
                else:
                    prev = temp
                    temp = temp.next

    def add_tail(self, value):
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = Node(value)






a = linkedlist()
a.add(1)
a.add(2)
a.add(3)
a.add(100)
a.add(1)
a.add(5)
a.add(1)
a.add(2)
a.add(3)
print(a.__str__())
print(a.search(1))
a.remove(2)
a.add_tail(8)
print(a.__str__())
print(a.search_all(1))


