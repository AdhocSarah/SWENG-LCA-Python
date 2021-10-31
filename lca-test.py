import unittest
from lca import Node, findLCA


class LCATest(unittest.TestCase):
    root = None

    def setUp(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        n5 = Node(5)
        n6 = Node(6)
        n7 = Node(7)
        self.root = n1
        n1.addChild(n2)
        n1.addChild(n3)
        n2.addChild(n4)
        n2.addChild(n5)
        n3.addChild(n6)
        n3.addChild(n7)

    def test_empty(self):
        root = None
        self.assertEqual(-1, findLCA(root, 1, 2))

    def test_valid(self):
        self.assertEqual(2, findLCA(self.root, 4, 5))
        self.assertEqual(1, findLCA(self.root, 4, 6))
        self.assertEqual(1, findLCA(self.root, 3, 4))
        self.assertEqual(2, findLCA(self.root, 2, 4))

    def test_invalid(self):
        self.assertEqual(-1, findLCA(self.root, 4, 8))

    def test_dag(self):
        n9 = Node(9)
        n10 = Node(10)
        self.root.addChild(n9)
        self.root.addChild(n10)
        self.assertEqual(1, findLCA(self.root, 9, 10))
        n9.addChild(self.root)
        self.assertEqual(-1, findLCA(self.root, 1, 9))




if __name__ == '__main__':
    unittest.main()
