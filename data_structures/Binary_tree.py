#  Copyright (c) 2021.
#  Mikhail Popkov (mihel-98@yandex.ru)
"""

Binary tree and operations with it

"""


class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        """
        Compare the new value with the parent node
        :param data: integer numbers
        """
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data),
        if self.right:
            self.right.print_tree()

    def inorder_traversal(self, root):
        """
        Inorder traversal
        Left -> Root -> Right

        """
        temp_res = []
        if root:
            temp_res = self.inorder_traversal(root.left)
            temp_res.append(root.data)
            temp_res = temp_res + self.inorder_traversal(root.right)
        return temp_res

    def preorder_traversal(self, root):
        """
        Preorder traversal
        Root -> Left ->Right
        :param root: integer numbers
        :return: list
        """
        temp_res = []
        if root:
            temp_res.append(root.data)
            temp_res = temp_res + self.preorder_traversal(root.left)
            temp_res = temp_res + self.preorder_traversal(root.right)
        return temp_res

    def postorder_traversal(self, root):
        """
        Postorder traversal
        Left ->Right -> Root
        :param root: integer numbers
        :return: list
        """
        temp_res = []
        if root:
            temp_res = self.postorder_traversal(root.left)
            temp_res = temp_res + self.postorder_traversal(root.right)
            temp_res.append(root.data)
        return temp_res
