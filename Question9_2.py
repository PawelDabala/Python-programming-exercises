"""
Question 9
Level 2

Question��
Write a program that accepts sequence of lines as input and prints the lines after making all
characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
"""
def make_upper(txt):
    return txt.upper()

text = """Hello world
Practice makes perfect
"""
print(make_upper(text))