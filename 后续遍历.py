class Node:
    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value


def method(node):
    if node.left:
        method(node.left)
    if node.right:
        method(node.right)
    print(node.value)


if __name__ == '__main__':
    node5 = Node(None, None, 5)
    node3 = Node(None, None, 3)
    node4 = Node(None, None, 4)
    node1 = Node(node3, None, 1)
    node2 = Node(node4, node5, 2)
    root = Node(node1, node2, 'root')
    method(root)
