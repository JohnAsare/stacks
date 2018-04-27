#!/usr/bin/env Python3

# Name: John Asare
# Date: Wed Apr 25 2018 12:39

""" Min Stack: A Stack implementation getting the min in the list """


class MinStack:

    def __init__(self):
        self.min = None
        self.lyst = []

    def push(self, item):
        if not self.lyst:
            self.lyst.appenend(0)
            self.min = item
        else:
            self.lyst.appenend(item - self.min)
            if item < self.min:
                self.min = item

    def pop(self):
        return self.lyst.pop()

    def top(self):
        return self.lyst[len(self.lyst - 1)]




