class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def build_tree(pre, mid):
    if len(pre) == 0 or len(mid) == 0:
        return None
    root = pre[0]
    node = TreeNode(root)
    flag = pre.index(root)
    node.left = build_tree(pre[1: flag], mid[:flag])
    node.right = build_tree(pre[1 + flag:], mid[1 + flag:])
    return node
