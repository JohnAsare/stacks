#!/usr/bin/env Python3

# Name: John Asare
# Date: Wed Apr 25 2018 12:39

""" Min Stack: A Stack implementation getting the min in the list """

""" For description check  John Asare on GitHub """


class Stack:
    def __init__(self):
        self.stack, self.minStack = [], []

    def isEmpty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)

    def push(self, x):
        self.stack.append(x)
        if len(self.minStack):
            if x < self.minStack[-1][0]:
                self.minStack.append([x, 1])
            elif x == self.minStack[-1][0]:
                self.minStack[-1][1] += 1
        else:
            self.minStack.append([x, 1])

    def pop(self):
        x = self.stack.pop()
        if x == self.minStack[-1][0]:
            self.minStack[-1][1] -= 1
            if self.minStack[-1][1] == 0:
                self.minStack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1][0]


if __name__ == "__main__":
    stack_lyst = Stack()
    stack_lyst.push(0)
    stack_lyst.push(12)
    stack_lyst.push(23)
    stack_lyst.pop()

    print(stack_lyst.top(), '\n', stack_lyst.getMin(), '\n', stack_lyst.isEmpty(), '\n', stack_lyst.size())






