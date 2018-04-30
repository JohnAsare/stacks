#!/usr/bin/env Python3

# Name: John Asare
# Date: Wed Apr 25 2018 12:39

""" Min Stack: A Stack implementation getting the min in the list """

""" For description check  John Asare on GitHub """

class Stack:

    def __init__(self):
        self.stack, self.Minstack = [],[]

    def push(self, item):
        self.stack.append(item)
        if len(self.Minstack):
            if item < self.Minstack[-1][0]:
                self.Minstack.append([item, 1])
            elif item == self.Minstack[-1][0]:
                self.Minstack[-1][1] += 1
        else:
            self.Minstack.append([item, 1])

    def pop(self):
        item = self.stack.pop()
        if item == self.Minstack[-1][0]:
            self.Minstack[-1][1] += -1

            if self.Minstack[-1][1] == 0:
                self.Minstack.pop()

    def getMin(self):
        return self.Minstack[-1][0]

    def peek(self):
        return self.stack[-1]

    def isEmpty(self):
        return self.stack == 0

    def size(self):
        return len(self.stack)


if __name__ == "__main__":
    stack_lyst = Stack()
    stack_lyst.push(0)
    stack_lyst.push(12)
    stack_lyst.push(23)
    stack_lyst.pop()

    print(stack_lyst.peek(), '\n', stack_lyst.getMin(), '\n', stack_lyst.isEmpty(), '\n', stack_lyst.size())






