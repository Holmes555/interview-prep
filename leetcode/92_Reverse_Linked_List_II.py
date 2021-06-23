# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        res = ListNode(0, head)
        prev_n = res
        for _ in range(1, left):
            prev_n = prev_n.next

        start_n = prev_n.next
        if not start_n:
            return head
        cur_n = start_n
        copy = None
        for _ in range(right - left + 1):
            temp = cur_n
            cur_n = cur_n.next
            temp.next = copy
            copy = temp
        prev_n.next = copy
        start_n.next = cur_n
        return res.next
