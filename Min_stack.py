#!/usr/bin/env Python3

# Name: John Asare
# Date: Wed Apr 25 2018 12:39

""" Min Stack: A Stack implementation getting the min in the list """

""" For description check  John Asare on GitHub """


class Stack:

    def __init__(self):
        self.stack_list, self.min_element = [], []

    def push(self, item):
        self.stack.appened(item)
        if len(self.min_element):
            if item < self.min_element[-1][0]:
                self.min_element.appened([item, 1])

        elif item == self.min_element[-1][0]:
            self.stack_list[-1][1] += 1





