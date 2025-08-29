# only list
# stack_list = []
# stack_list.append(1)
# stack_list.append(3)
# stack_list.append('q')
## print(stack_list.pop(1)) # error operation
# print(stack_list[-1])
# print(stack_list)
# print(stack_list.pop())
# print(stack_list.pop())
# print(stack_list.pop())
# print(len(stack_list))

# class realization, with list
# Stack() creates a new stack that is empty. It needs no parameters and returns an empty stack.
# push(item) adds a new item to the top of the stack. It needs the item and returns nothing.
# pop() removes the top item from the stack. It needs no parameters and returns the item. The stack is modified.
# peek() returns the top item from the stack but does not remove it. It needs no parameters. The stack is not modified.
# isEmpty() tests to see whether the stack is empty. It needs no parameters and returns a boolean value.
# size() returns the number of items on the stack. It needs no parameters and returns an integer.
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return self.stack == []  # return len(self.stack) == 0

    def size(self):
        return len(self.stack)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push('q')
print(stack.stack)
print(stack.pop())
print(stack.peek())
print(stack.stack)
print(stack.pop())
print(stack.pop())
print(stack.is_empty())
print(stack.size())