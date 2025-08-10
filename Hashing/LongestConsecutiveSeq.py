def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        s = set(nums)
        longest = 0
        for i in s:
            if i-1 not in s:
                next_num = i+1
                length = 1
                while next_num in s:
                    length+=1
                    next_num+=1
                longest = max(longest, length)
        return longest