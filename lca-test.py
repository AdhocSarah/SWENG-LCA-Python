import unittest
from lca import Node, findLCA




class LCATest(unittest.TestCase):


    def test_empty(self):
        root = None
        self.assertEqual(-1, findLCA(root, 1, 2))



    def test_valid(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        self.assertEqual(2, findLCA(root, 4, 5))
        self.assertEqual(1, findLCA(root, 4, 6))
        self.assertEqual(1, findLCA(root, 3, 4))
        self.assertEqual(2, findLCA(root, 2, 4))

    def test_invalid(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        self.assertEqual(-1, findLCA(root, 4, 8))

if __name__ == '__main__':
    unittest.main()