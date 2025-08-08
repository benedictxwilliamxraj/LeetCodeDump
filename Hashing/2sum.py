def twoSum(self, nums: List[int], target: int) -> List[int]:
        #brute force -> two pointers 
        # for i in range(len(nums)):
        #     diff = target - nums[i]
        #     for j in range(i+1, len(nums)):
        #         if diff == nums[j]:
        #             return [i, j]
        # return []
        
        #Implementation using hashing
        hp = {}
        for i in range(len(nums)):
            hp[nums[i]] = i
        for i in range(len(nums)):
            y = target - nums[i]

            if y in hp and hp[y]!=i:
                return [i, hp[y]]
        
        return []
