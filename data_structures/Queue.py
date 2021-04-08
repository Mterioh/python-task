#  Copyright (c) 2021.
#  Mikhail Popkov (mihel-98@yandex.ru)
"""

Queue and operations with it

"""


class Queue:

    def __init__(self):
        self.queue = list()

    def add_toq(self, data_val):
        """
        Insert method to add element
        """
        if data_val not in self.queue:
            self.queue.insert(0, data_val)
            return True
        return False

    def remove_from_q(self):
        """
        Pop method to remove element
        """
        if len(self.queue) > 0:
            return self.queue.pop()
        return "No elements in Queue!"
