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

    def add(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            temp = [self.root]
            while True:
                pop_node = temp.pop(0)
                if pop_node.left is None:
                    pop_node.left = new_node
                    return
                elif pop_node.right is None:
                    pop_node.right = new_node
                    return
                else:
                    temp.append(pop_node.left)
                    temp.append(pop_node.right)

    def get_parent(self, data):
        if self.root.data == data:
            return None
        temp = [self.root]
        while temp:
            pop_node = temp.pop(0)
            if pop_node.left:
                if pop_node.left.data == data:
                    return pop_node
                else:
                    temp.append(pop_node.left)
            if pop_node.right:
                if pop_node.right.data == data:
                    return pop_node
                else:
                    temp.append(pop_node.right)
        return None


if __name__ == '__main__':
    binary = BinaryTree()
    for i in range(10):
        binary.add(i)
    print(binary.root.left.left.right)
