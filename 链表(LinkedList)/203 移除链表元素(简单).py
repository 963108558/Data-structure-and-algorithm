# 思想:虚拟节点

# 删除链表中等于给定值 val 的所有节点。
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        while current.next:
            temp = current.next
            if temp.val == val:
                current.next = current.next.next
                temp.next = None
            else:
                current = current.next
        return dummy.next