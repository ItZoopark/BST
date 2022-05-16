class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        # return self

    def contains(self, value):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True
        return False

    def remove(self, value, parentNode=None):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                # case with two children
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinValue()
                    currentNode.right.remove(currentNode.value, currentNode)
                # root case
                elif parentNode is None:
                    if currentNode.left is not None:
                        if currentNode.left is not None:
                            currentNode.value = currentNode.left.value
                            currentNode.right = currentNode.left.right
                            currentNode.left = currentNode.left.left
                        elif currentNode.right is not None:
                            currentNode.value = currentNode.right.value
                            currentNode.left = currentNode.right.left
                            currentNode.right = currentNode.right.right
                # case with one child
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
                break

    def getMinValue(self):
        if self.left is None:
            return self.value
        else:
            return self.left.getMinValue()


# root = BST(10)
# root.left = BST(5)
# root.left.left = BST(2)
# root.left.left.left = BST(1)
# root.left.right = BST(5)
# root.right = BST(15)
# root.right.left = BST(13)
# root.right.left.right = BST(14)
# root.right.right = BST(22)
# root.insert(12)
# print(root.right.left.left.value == 12)
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BST(10)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.right = BST(5)
        root.right = BST(15)
        root.right.left = BST(13)
        root.right.left.right = BST(14)
        root.right.right = BST(22)

        root.insert(12)
        self.assertTrue(root.right.left.left.value == 12)

        root.remove(10)
        self.assertTrue(not root.contains(10))
        self.assertTrue(root.value == 12)

        self.assertTrue(root.contains(15))
