class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __repr__(self):
        return f'Node({self.data})'


class BinaryTree:
    def __init__(self):
        self.root = None

    # 前序遍历
    def preOrderTreverse(self, node):
        if not node:
            return None
        print(node.value)
        self.preOrderTreverse(node.left)
        self.preOrderTreverse(node.right)

    # 中序遍历
    def preOrderTreverse1(self, node):
        if not node:
            return None
        self.preOrderTreverse1(node.left)
        print(node.value)
        self.preOrderTreverse1(node.right)
