# imports go on their own line
import sys
import os


# two blank lines to separate classes from other functions
class Myclass():
    def __init__(self):
        self.prop1 = "my class"

    # within class, one blank line separates methods
    def method1(self, arg1):
        pass


def main():
    # Long comments, like this one that flow accross several lines, are
    # limited to 72 characters instead of 79 for lines of code
    cls1 = Myclass()
    cls1.prop1 = "hello world"
