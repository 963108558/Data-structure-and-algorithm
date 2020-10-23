# 思想:虚拟节点
#
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
# and方法
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        prev = dummy
        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        if l1 is None:
            prev.next = l2
        if l2 is None:
            prev.next = l1
        return dummy.next
# or 方法
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_node = ListNode(0)
        prev = new_node
        while l1 or l2:
            if l1 is None:
                prev.next = l2
                break
            if l2 is None:
                prev.next = l1
                break
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        return new_node.next