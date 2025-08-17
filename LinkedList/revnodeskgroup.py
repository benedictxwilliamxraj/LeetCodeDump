# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def rev(thead):
            prev = None
            curr = thead
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            #print(prev)
            return prev

        # setup a counter, when divisible by k => call the fun rev
        cnt = 1
        curr = head
        dum = ListNode(0)
        dum.next = head
        prev = dum
        thead = head
        while curr:

            if cnt % k == 0:
                temp = curr.next
                print(thead)
                curr.next = None
                a = rev(thead)
                prev.next = a 
                thead.next = temp
                curr = thead
                prev = thead
                thead = thead.next
                
            curr = curr.next
            cnt+=1
        return dum.next