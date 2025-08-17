# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = ListNode(0)
        prev.next = head
        dum = prev
        curr = head
        while curr and curr.next:
            # Store b.next in temp
            # attach boogies of b.next into a
            # b.next into a
            # Connect the prev boogie into b
            # Increment the pointer
            a = curr
            b = curr.next
            temp = b.next
            #print(temp)
            a.next = temp
            #print(a)
            b.next = a
            prev.next = b
            print(curr)
            prev = curr
            curr = curr.next
            
        #print(head)
        return dum.next
            