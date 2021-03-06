#!/usr/bin/env Python 3

# Name: John Asare
# Date: Mon Apr 23 0:14

""" Stacks algorithm implementation """


class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


s = Stack()
s.push(1)
s.push(12)
s.push("dog")
s.pop()

print(s.size())
print(s.peek())


