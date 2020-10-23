class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'Node({self.data})'


class LinkQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, data):
        node = Node(data)
        if self.is_emity():
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        self.size += 1

    def dequeue(self):
        if self.is_emity():
            raise IndexError('错误')
        else:
            node = self.front
            self.front = self.front.next
            node.next = None
            self.size -= 1
        return node

    def is_emity(self):
        return self.front is None

    def __repr__(self):
        current = self.front
        string = ''
        while current:
            string += f'{current}-->'
            current = current.next
        return string + 'END'


if __name__ == '__main__':
    queue = LinkQueue()
    for i in range(5):
        queue.enqueue(i)
    queue.dequeue()
    print(queue)
