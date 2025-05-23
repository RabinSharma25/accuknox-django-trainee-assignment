# rectangle.py
'''
Topic: Custom Classes in Python
Description: You are tasked with creating a Rectangle class with the following requirements:
1. An instance of the Rectangle class requires length:int and width:int to be
initialized.
2. We can iterate over an instance of the Rectangle class
3. When an instance of the Rectangle class is iterated over, we first get its length in the
format: {'length': <VALUE_OF_LENGTH>} followed by the width {width:
<VALUE_OF_WIDTH>}



Answer :-
✅ Requirements Recap
The class should accept length and width when initialized.

It should be iterable.

Iteration over the object should yield:

{'length': <value>}

{'width': <value>}

✅ Solution
We’ll use the __iter__() method to make the object iterable.
'''
class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}
