# PEP 8 coding style https://www.python.org/dev/peps/pep-0008/
# imports go on their won lines
import sys
import os


# two blank lines separate classes from other functions
class MyClass():
    def __init__(self):
        self.prop1 = "my class"

    # within classes, one blank line separates methods
    def method1(self, arg1):
        pass


def main():
    # Long comments, like this one that flow across serval lines, are
    # limited to 72 characters instead of 79 for lines of code.
    cls1 = myClass()
    cls1.prop1 = "hello world"