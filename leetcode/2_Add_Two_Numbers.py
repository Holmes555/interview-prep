# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = 0
        i = 0
        while l1 is not None or l2 is not None:
            if l1 is not None:
                res += 10**i * l1.val
                l1 = l1.next
            if l2 is not None:
                res += 10**i * l2.val
                l2 = l2.next
            i += 1

        res_l = None
        i = len(str(res)) - 1
        while i >= 0:
            num = int(res // 10**i) % 10
            res_l = ListNode(num, res_l)
            i -= 1
        return res_l


class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = 0
        i = 0
        while l1 is not None or l2 is not None:
            if l1 is not None:
                res += 10**i * l1.val
                l1 = l1.next
            if l2 is not None:
                res += 10**i * l2.val
                l2 = l2.next
            i += 1

        res_l = None
        i = len(str(res)) - 1
        while i >= 0:
            num = int(res // 10**i) % 10
            res_l = ListNode(num, res_l)
            i -= 1
        return res_l
