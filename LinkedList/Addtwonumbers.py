
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        currCarry = 0
        p1 = l1
        p2 = l2
        curr = head = ListNode(0)
        while p1 or p2 or currCarry:
            currVal = currCarry
            currVal+= 0 if p1 is None else p1.val
            currVal+= 0 if p2 is None else p2.val
            if currVal >= 10:
                currVal = currVal - 10
                currCarry = 1
            else:
                currCarry = 0
            curr.next = ListNode(currVal)
            curr = curr.next
            if p1 is None and p2 is None:
                break
            elif p1 is None:
                p2 = p2.next
            elif p2 is None:
                p1 = p1.next
            else:
                p1 = p1.next
                p2 = p2.next
        
        return head.next