# Code review
class Node:
    def __init__(self, val=None):
        self.val = val
        self.right = None
        self.left = None


def is_leaf(node):
    if not node:
        return False
    return node.left is None and node.right is None


def find_number_of_nodes_in_last_level(node):
    if node:
        right_is_leaf = False
        if node.right is not None:
            right_is_leaf = is_leaf(node.right)
        left_is_leaf = False
        if node.left is not None:
            left_is_leaf = is_leaf(node.left)
        if left_is_leaf or right_is_leaf:
            return 1 + find_number_of_nodes_in_last_level(node.left) + find_number_of_nodes_in_last_level(node.right)
        else:
            return 0 + find_number_of_nodes_in_last_level(node.left) + find_number_of_nodes_in_last_level(node.right)
    else:
        return 0


def test1():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.left = Node(5)
    if find_number_of_nodes_in_last_level(root) == 3:
        print('Test 1 : Success')
    else:
        print('Test 1 : Failure')


def test2():
    root = Node(1)
    if find_number_of_nodes_in_last_level(root) == 0:
        print('Test 2 : Success')
    else:
        print('Test 2 : Failure')


def test3():
    root = Node(1)
    root.left = Node(2)
    if find_number_of_nodes_in_last_level(root) == 1:
        print('Test 3 : Success')
    else:
        print('Test 3 : Failure')


test1()
test2()
test3()
