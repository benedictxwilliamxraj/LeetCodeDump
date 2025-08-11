def subarraySum(self, nums: List[int], k: int) -> int:
        
        # Create hasha with key st indx and array of list with its sum
        # iterate through hp where prsum = k
        # hp = {}
        # for i in range(len(nums)):
        #     a = []
        #     psum = 0
        #     for j in range(i,len(nums)):
        #         psum+=nums[j]
        #         a.append(psum)

        #     hp[i] = a
        
        # cnt =0
        # print(hp)
        # for i in hp.values():
        #     for j in i:
        #         if k == j:
        #             cnt+=1
        
        # return cnt
        # Above get memory exceeded limit

        # T(n) = O(N) Space: O(N)
        count = 0
        prefix = 0
        seen = defaultdict(int)
        seen[0] = 1            

        for x in nums:
            prefix += x
            # how many previous prefixes equal to prefix - k?
            count += seen[prefix - k]
            seen[prefix] += 1
        print(seen)
        return count


