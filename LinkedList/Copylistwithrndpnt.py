"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        curr = head
        hp = {}
        # map nodes in dict
        while curr:
            copy = Node(curr.val)
            hp[curr] = copy
            curr = curr.next
        curr = head
        while curr:
            new_node = hp[curr]
            new_node.next = hp[curr.next] if curr.next else None
            new_node.random = hp[curr.random] if curr.random else None
            curr = curr.next
        
        return hp[head]
