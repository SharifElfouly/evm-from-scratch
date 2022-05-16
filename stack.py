from number import Number

class StackTooLargeException(Exception):
    pass
class StackEmptyException(Exception):
    pass

class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) == 0: raise StackEmptyException()

        return self.stack.pop().value

    def push(self, value):
        if len(self.stack) > 1024: raise StackTooLargeException()

        self.stack.append(Number(value))

    def __str__(self): return " ".join([str(x) for x in self.stack])
