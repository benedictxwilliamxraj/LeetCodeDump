# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find the lenght using counter
        # again for loop to remove the element
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        nthele = length - n +1
        print(length, nthele)
        
        curr = head
        cnt = 1
        prev = None
        while curr:
            if nthele == cnt:
                if prev is None:
                    head = head.next
                else:
                    prev.next = curr.next
            cnt+=1
            prev = curr
            curr = curr.next
        return head