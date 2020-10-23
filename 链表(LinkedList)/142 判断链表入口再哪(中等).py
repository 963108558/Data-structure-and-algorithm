# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
# 如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。
# 说明：不允许修改给定的链表。

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while True:
                    if slow == fast:
                        return slow
                    slow = slow.next
                    fast = fast.next
        return

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
        # 如果快指针和慢指针相遇
        if fast == slow:
            # 结束循环
            break
    # 如果快指针和慢指针相遇,证明是一个环
    if fast == slow:
        # 让慢指针从头开始
        slow = head
        # 通过数学公式得到以下代码的正确性
        while slow != fast:
            # 慢指针走一步
            slow = slow.next
            # 快指针走一步
            fast = fast.next
        # 相遇的点就是入口点
        return slow


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