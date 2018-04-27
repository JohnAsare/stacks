#!/usr/bin/env Python3

# Name: John Asare
# Date: Wed Apr 25 2018 12:39

""" Min Stack: A Stack implementation getting the min in the list """

""" For description check  John Asare on GitHub """


class Stack:

    def __init__(self):
        self.stack_list, self.min_element = [], []

    def push(self, item):
        self.stack_list.append(item)
        if len(self.min_element):
            if item < self.min_element[-1][0]:
                self.min_element.append([item, 1])

        elif item == self.min_element[-1][0]:
            self.min_element[-1][1] += 1

        else:
            self.stack_list.append([item, 1])

    def pop(self):
        smallest_item = self.stack_list.pop()
        if smallest_item == self.min_element[-1][0]:
            self.min_element[-1][1] -= 1

            if self.min_element[-1][1] == 0:
                self.min_element.pop()

    def peek(self):
        return self.stack_list[-1]

    def getMin(self):
        return self.min_element[-1][0]


if __name__ == "__main__":
    stack_lyst = Stack()
    stack_lyst.push(-1)

    print(stack_lyst.top(), stack_lyst.getMin())






