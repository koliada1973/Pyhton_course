class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        else:
            self.index -= 1
            return self.data[self.index]

my_str = 'python'
for e in my_str:
    print(e, end='')
print()

for elem in Reverse(my_str):
    print(elem, end='')
print()


def Reverse(data):
    for i in range(len(data) - 1, -1, -1):
        yield data[i]

for elem in Reverse(my_str):
    print(elem, end='')
