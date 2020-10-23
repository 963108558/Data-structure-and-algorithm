# 思想:快慢指针

# 创建结点类
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'Node({self.data})'


# 创建判断链表是否有环的函数
def Just(head: Node):
    # 快指针定义
    fast = head
    # 慢指针定义
    slow = head
    # 如果快指针和快指针的下一个结点一直不为空
    while fast and fast.next:
        # 快指针一次走两步
        fast = fast.next.next
        # 慢指针一次走一步
        slow = slow.next
        # 如果快指针和慢指针相遇(返回True)
        if fast == slow:
            return True
    # 如果fast或者fast.next循环到is None,表明没有环(返回False)
    return False


# 创建链表
if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node3

# 调用函数(判断结果)
print(Just(node1))
