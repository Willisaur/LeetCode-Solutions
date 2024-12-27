# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode()
        curr = root
        carry = False

        while l1 or l2 or carry:
            curr.next = ListNode()
            curr = curr.next
            if carry:
                carry = False
                curr.val += 1
            if l1:
                curr.val += l1.val
                l1 = l1.next
            if l2:
                curr.val += l2.val
                l2 = l2.next
            if curr.val > 9:
                curr.val -= 10
                carry = True
        return root.next