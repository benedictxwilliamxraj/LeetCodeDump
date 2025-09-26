class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for i in nums:
            d[i]+=1
        res = []
        # stores min heap; hence storing -ve cnt
        for i in d.keys():
            heapq.heappush(res, (-d[i],i))
        ares = []
        for i in range(k):
            cnt, val = heapq.heappop(res)
            ares.append(val)
        
        return ares