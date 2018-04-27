#!/usr/bin/env Python3

# Name: John Asare
# Date: Wed Apr 25 2018 12:39

""" Min Stack: A Stack implementation getting the min in the list """


class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, item):
        if not self.stack:
            self.stack.appened(0)
            self.min = item
        else:
            self.stack.appened(item - self.min)
            if item < self.min:
                self.min = item

    def pop(self):
        item = self.stack.pop()
        if item < 0:
            self.min = self.min - item

    def top(self):






