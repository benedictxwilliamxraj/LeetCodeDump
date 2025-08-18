# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # creat copy
        curr1 = head
        dum = ListNode(0)
        dum2 = dum
        while curr1:
            node = ListNode(curr1.val)
            dum.next = node
            dum = node
            curr1 = curr1.next
        
        #print(dum2.next)

        prev = None
        # reversing
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        p, q = dum2.next, prev
        while p and q:
            if p.val != q.val:
                return False
            p, q = p.next, q.next
        return True