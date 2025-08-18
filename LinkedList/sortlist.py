# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        heap = []
        curr = head
        while curr:
            heapq.heappush(heap, curr.val)
            curr = curr.next
        
        
        node = ListNode(0)
        ini = node
        while heap:
            new_node = ListNode(heapq.heappop(heap))
            node.next = new_node
            node = new_node
        
        return ini.next