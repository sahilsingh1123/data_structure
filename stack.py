#! /usr/bin/env python

class stack:


    def __init__(self):
        self.stack = []


    def isempty(self):
        return self.stack == []


    def push(self,data):
        self.stack.append(data)


    def pop(self):

        data = self.stack[-1]
        del self.stack[-1]
        return data

    def peek(self):
        return self.stack[-1]


    def sizestack(self):
        return len(self.stack)






stackk = stack()

stackk.push(12)
stackk.push(129)
stackk.push(168)
stackk.push(15)


print(stackk.sizestack())

print(stackk.pop())
print(stackk.pop())
print(stackk.pop())


print("peek", stackk.peek())

print("size of stack is", stackk.sizestack())
