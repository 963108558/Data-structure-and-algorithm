class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'Node({self.data})'


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # 查找下标结点
    def get(self, index):
        current = self.head
        # 方案1
        for _ in range(index):
            current = current.next
        # 方案2
        # j = 0
        # while j < index:
        #     current = current.next
        #     j += 1
        return current

    # 添加结点
    def insert(self, index, data):
        new_node = Node(data)
        if index < 0 or index > self.size:
            raise IndexError('Index输入错误')
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        elif index == self.size:
            self.tail.next = new_node
            self.tail = new_node
        else:
            prev = self.get(index - 1)
            new_node.next = prev.next
            prev.next = new_node
        self.size += 1

    # 打印链表
    def __repr__(self):
        current = self.head
        string = ''
        while current:
            string += f'{current}-->'
            current = current.next
        return string + 'END'

    # 删除结点
    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError('Index输入错误')
        if index == 0:
            remove_node = self.head
            self.head = self.head.next
            remove_node.next = None
        elif index == self.size - 1:
            prev = self.get(index - 1)
            remove_node = prev.next
            prev.next = None
            self.tail = prev
        else:
            prev = self.get(index - 1)
            remove_node = prev.next
            prev.next = prev.next.next
            remove_node.next = None
        self.size -= 1
        return remove_node

    def reverse(self):
        prev = None
        current = self.head
        while current:
            new_node = current.next
            current.next = prev
            prev = current
            current = new_node
        self.head = prev

    # 删除固定的元素
    def removes(self, object: Node):
        new_node = f'Node({object})'
        current = self.head
        if self.size is None:
            raise IndexError('为空链表')
        while current:
            prev = current.next
            if prev == new_node:
                # prev = current.next
                current.next = current.next.next
                prev.next = None
            else:
                current = current.next


result = LinkedList()
for i in range(5):
    result.insert(0, i)
result.insert(1, 4)
result.insert(4, 4)
result.insert(6, 4)
result.removes(4)
# print(result.get(2))
# print(result.remove(2))
print(result)
