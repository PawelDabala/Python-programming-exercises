"""
Question 5
Level 1

Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

"""
class GetText():


    def __init__(self,stext):
        self.stext = stext


    def print_text(self):
        print(self.stext.upper())

test = GetText("Super")
test.print_text()

class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = raw_input()

    def printString(self):
        print self.s.upper()

strObj = InputOutString()
strObj.getString()
strObj.printString()