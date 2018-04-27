#!/usr/bin/env Python3

# Name: John Asare
# Date: Wed Apr 25 2018 12:39

""" Min Stack: A Stack implementation getting the min in the list """


class MinStack:

    def __init__(self):
        self.lyst = []

    def push(self, x):
        self.lyst.append(x)

    def pop(self):
        return self.lyst.pop()

    def top(self):
        return self.lyst[len(self.lyst - 1)]

sddsf


