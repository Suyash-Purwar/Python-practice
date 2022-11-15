class Stack:
    list1 = []

    def push(self, data):
        self.list1.append(data)

    def pop(self):
        return self.list1.pop()

stack1 = Stack()
stack1.push(12)
stack1.push(212)
stack1.push(142)
stack1.push(125)
stack1.push(124)

for i in stack1.list1:
    print(i, end=" ")
print()

print(stack1.pop())

for i in stack1.list1:
    print(i, end=" ")
print()