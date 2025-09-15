# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        y = n-k+1
        heapq.heapify(nums)
        for i in range(y):
            min1 = heapq.heappop(nums)
        return min1