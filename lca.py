# Obtained from https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/
# Python Program for Lowest Common Ancestor in a Binary Tree
# O(n) solution to find LCS of two given values n1 and n2

# A binary tree node
class Node:
    # Constructor to create a new binary node
    def __init__(self, key):
        self.key = key
        self.children = []

    def addChild(self, child):
        self.children.append(child)


# Finds the path from root node to given root of the tree.
# Stores the path in a list path[], returns true if path
# exists otherwise false

def findPath(root, path, k):
    # Base Case
    if root is None:
        return False

    # Store this node is path vector. The node will be
    # removed if not in path from root to k

    if root.key in path:
        return False
    else:
        path.append(root.key)

    # See if the k is same as root's key
    if root.key == k:
        return True

    # Check if k is found in left or right sub-tree
    for child in root.children:
        if findPath(child, path, k) == 1:
            return True

    # If not present in subtree rooted with root, remove
    # root from path and return False

    path.pop()
    return False


def isAcyclic(root):
    if not root:
        return True
    if len(root.children) == 0:
        return True
    return isAcyclicRec(root, [])


def isAcyclicRec(root, path):
    if root in path:
        return False
    acyc = True
    path.append(root)
    for child in root.children:
        if not isAcyclicRec(child, path):
            acyc = False
    return acyc


# Returns LCA if node n1 , n2 are present in the given
# binary tre otherwise return -1
def findLCA(root, n1, n2):
    if not isAcyclic(root):
        return -1

    # To store paths to n1 and n2 from the root
    path1 = []
    path2 = []

    # Find paths from root to n1 and root to n2.
    # If either n1 or n2 is not present , return -1
    if not findPath(root, path1, n1) or not findPath(root, path2, n2):
        return -1

    # Compare the paths to get the first different value
    i = 0
    while i < len(path1) and i < len(path2):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i - 1]
