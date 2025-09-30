# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh = 0
        q = deque()
        time = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh+=1
                if grid[i][j] == 2:
                    q.append([i,j])
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in ([1,0], [0,1], [0,-1], [-1,0]):
                    row = r+dr
                    col = c+dc
                    if  (row in range(m)) and (col in range(n)) and grid[row][col]==1:
                        grid[row][col] = 2
                        fresh-=1
                        q.append([row,col])
            time+=1
        
        return time if fresh==0 else -1
