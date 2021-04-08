#  Copyright (c) 2021.
#  Mikhail Popkov (mihel-98@yandex.ru)
"""

Binary tree and operations with it

"""


class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)
