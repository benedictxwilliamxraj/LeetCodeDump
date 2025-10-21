# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n: int) -> int:
        #decision tree
        # print n fib seq
        arr = [1,2]
        if n == 1:
            return arr[0]
        if n == 2:
            return arr[1]
        for i in range(2,n):
            arr.append(arr[-1]+arr[-2])
        
        return arr[-1]