class Element_Deque:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class MyDeque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size_deque = 0

    def addFront(self, data):
        temp = Element_Deque(data)
        self.size_deque += 1
        if self.head == self.tail == None:
            self.head = self.tail = temp
        else:
            self.head.prev = temp
            temp.next = self.head
            self.head = temp

    def addRear(self, data):
        temp = Element_Deque(data)
        self.size_deque += 1
        if self.tail == self.head == None:
            self.tail = self.head = temp
        else:
            self.tail.next = temp
            temp.prev = self.tail
            self.tail = temp

    def removeFront(self):
        if self.isEmpty():
            raise IndexError("MyDeque is empty")
        self.size_deque -= 1
        temp = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return temp.data

    def removeRear(self):
        if self.isEmpty():
            raise IndexError("MyDeque is empty")
        self.size_deque -= 1
        temp = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return temp.data

    def isEmpty(self):
        return self.head == self.tail == None

    def size(self):
        return self.size_deque


d = MyDeque()
d.addRear(4)
d.addRear("dog")
d.addFront("cat")
d.addFront(True)
print(d.size())
print(d.isEmpty())