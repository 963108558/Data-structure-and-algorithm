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
        stack = [node]
        while len(stack) > 0:
            print(node.value)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            node = stack.pop()

    # 中序遍历
    def preOrderTreverse1(self, node):
        stack = []
        while node or len(stack) > 0:
            while node:
                stack.append(node)
                node = node.left
            if len(stack) > 0:
                node = stack.pop()
                print(node.value)
                node = node.right

    # 后序遍历
    def post_order_stack(self, node):
        stack1 = []
        stack2 = []
        stack1.append(node)
        while stack1:
            node = stack1.pop()
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
            stack2.append(node)
        while stack2:
            print(stack2.pop().value, sep='-->', end='')
