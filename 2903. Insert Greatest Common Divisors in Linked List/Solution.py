# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
        firstVal = head.val
        
        if head.next != None:
            secondVal = head.next.val
            secondAddr = head.next
        else:
            return head
        
        
        while (secondAddr != None):
            head.next = ListNode(math.gcd(firstVal, secondVal), next = secondAddr)
            
            head = head.next.next
            firstVal = head.val
            if head.next != None:
                secondVal = head.next.val
                secondAddr = head.next
            else:
                secondAddr = None
        
        return start