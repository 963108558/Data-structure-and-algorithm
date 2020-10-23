# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        pre = dummy
        current = head
        while current is not None:
            temp = current.next
            while pre.next is not None and pre.next.val < current.val:
                pre = pre.next
            current.next = pre.next
            pre.next = current
            current = temp
            pre = dummy
        return dummy.next
