from pprint import pformat  # (节点打印模块)


class Node:
    def __init__(self, value, parent):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.value)
        return pformat({'%s' % (self.value): (
            self.left, self.right)}, indent=1)


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def __repr__(self):
        return str(self.root)

    def is_empty(self):
        if self.root is None:
            return True
        return False

    def __insert(self, value):
        new_node = Node(value, None)
        if self.is_empty():
            self.root = new_node
        else:
            parent_node = self.root
            while True:
                if value < parent_node.value:
                    if parent_node.left is None:
                        parent_node.left = new_node
                        break
                    else:
                        parent_node = parent_node.left
                elif value >= parent_node.value:
                    if parent_node.right is None:
                        parent_node.right = new_node
                        break
                    else:
                        parent_node = parent_node.right
            new_node.parent = parent_node

    def insert(self, *values):
        for value in values:
            self.__insert(value)
        return self

    def search(self, value):
        if self.is_empty():
            raise IndexError('空的查啥啊')
        else:
            parent = self.root
            while parent and value != parent.value:
                if value < parent.value:
                    parent = parent.left
                elif value > parent.value:
                    parent = parent.right
            return parent

    def remove(self, value):
        if self.root is None:
            raise IndexError('错误')
        else:
            node = self.search(value)
            if node is not None:
                if node.left is None and node.right is None:
                    self._reassign_nodes(node, None)
                elif node.left is None:
                    self._reassign_nodes(node, node.rigt)
                elif node.right is None:
                    self._reassign_nodes(node, node.left)
                else:
                    temp_node = self.get_max(node.left)
                    self.remove(temp_node.value)
                    node.value = temp_node.value

    def _reassign_nodes(self, node, new_children):
        if new_children is not None:
            new_children.parent = node.parent
        if node.parent is not None:
            if self.is_right():
                node.parent.right = new_children
            else:
                node.parent.left = new_children
        else:
            self.root = new_children

    def get_max(self, left):
        pass

    def is_right(self):
        return self.node == self.node.parent.right


if __name__ == '__main__':
    binary = BinarySearchTree()
    result = binary.insert(8, 4, 5, 7, 2, 9)
    print(binary.search(4))
    print(result)
