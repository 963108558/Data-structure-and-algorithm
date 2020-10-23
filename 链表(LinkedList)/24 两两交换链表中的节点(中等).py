# 思路:虚拟节点

# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while prev.next and prev.next.next:
            # 指针上岗
            slow = prev.next
            fast = prev.next.next
            prev.next = fast
            slow.next = fast.next
            fast.next = slow
            prev = prev.next.next
        return dummy.next