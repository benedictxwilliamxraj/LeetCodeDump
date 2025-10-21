# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, 
# which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # min1 = [float('inf')]
        # m, n = len(grid), len(grid[0])
        
        # def minpathsum(i ,j):
        #     # if i == m-1 and j == n-1:
        #     #     return grid[i][j]
        #     if i == 0 and j == 0:
        #         return grid[0][0]
        #     if i<0 or j<0:
        #         return float('inf')
        #     top = minpathsum(i-1, j)
        #     left = minpathsum(i,j-1)
        #     # grid[i][j] += min(top, left)
        #     return grid[i][j] + min(top, left)
        # ans = minpathsum(m-1, n-1)
        # print(grid)
        # return ans   

        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue  # start cell stays same
                top  = grid[i-1][j] if i > 0 else float('inf')
                left = grid[i][j-1] if j > 0 else float('inf')
                grid[i][j] += min(top, left)

        return grid[m-1][n-1]    