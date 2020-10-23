from typing import List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return 'Node({})'.format(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, data):
        new_head = Node(data)
        if self.head is not None:
            new_head.next = self.head
        self.head = new_head

    def append(self, data):
        if self.head is not None:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)
        else:
            self.insert_head(data)

    def __repr__(self):
        current = self.head
        string_repr = ''
        while current:
            string_repr += '{}-->'.format(current)
            current = current.next
        return string_repr + 'END'

    def insert(self, i, data):
        if self.head is None:
            self.insert_head(data)
        elif i == 1:
            self.insert_head(data)
        else:
            temp = self.head
            j = 1
            pre = temp
            while j < i:
                pre = temp
                temp = temp.next
                j += 1
            node = Node(data)
            pre.next = node
            node.next = temp

    def LinkList(self, object: List):
        self.head = Node(object[0])
        temp = self.head
        for i in object[1:]:
            node = Node(i)
            temp.next = node
            temp = temp.next

    def delete_head(self):
        temp = self.head
        if self.head is not None:
            temp = temp.next

    def delete_lost(self):
        temp = self.head
        if self.head is not None:
            if self.head.next is None:
                self.head = None
            else:
                while temp.next.next is not None:
                    temp = temp.next
                temp.next = None
        else:
            print('链表为空')

    def reverse(self):
        prev = None
        curror = self.head
        while curror is not None:
            new = curror.next
            curror.next = prev
            prev = curror
            curror = new
        self.head = prev

    def __getitem__(self, index):
        current = self.head
        if current is None:
            raise IndexError('空链表')
        for _ in range(1, index):
            if current.next is None:
                raise IndexError('超出范围')
            current = current.next
        return current

    def get(self, index):
        return self.__getitem__(index)

    def __setitem__(self, index, data):
        current = self.head
        if current is None:
            raise IndexError('空链表')
        for _ in range(1, index):
            if current.next is None:
                raise IndexError('超出范围')
            current = current.next
        current.data = data

    def set(self, index, data):
        return self.__setitem__(index, data)


result = LinkedList()
# for i in range(6, 1, -1):
#     result.insert_head(i)
# result.append(1)
# result.insert(2, 10)
result.LinkList(list(range(5)))
result.delete_lost()
result.reverse()
# print(result.get(2))
print(result)
result.set(2, 10)
print(result)
