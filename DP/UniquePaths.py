# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). 
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
# The robot can only move either down or right at any point in time.


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # ibh
        memo = [[-1 for _ in range(n)] for _ in range(m)]
        def rob(i,j):
            # base case
            if i == m-1 and j == n-1:
                return 1
            if i >= m or j >= n:
                return 0
            if memo[i][j]!=-1:
                return memo[i][j]
            # hypothesis
            bottom = rob(i+1, j)
            right = rob(i, j+1)
            #print(i,j, bottom, right)
            # induction
            memo[i][j] = bottom + right
            # cnt = bottom + right

            return memo[i][j]
        ans = rob(0,0)
        print(memo)
        return ans
