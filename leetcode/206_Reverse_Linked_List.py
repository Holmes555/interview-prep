# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        n = m = head
        c = head.next

        while head:
            head = c.next
            c.next = n
            m.next = head
            n = c
            c = head

        return n


class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        copy = ListNode(head.val, head)
        head = head.next
        copy.next = None
        while head:
            temp = head
            head = head.next
            temp.next = copy
            copy = temp
        return copy
