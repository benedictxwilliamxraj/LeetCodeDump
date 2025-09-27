# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #q = deque()
        visited = set()
        m, n = len(grid), len(grid[0])
        def bfs(q):
            while q:
                #print(q)
                r, c = q.popleft()
                for dr,dc in ((1,0),(0,1),(-1,0),(0,-1)):
                    row = r+dr
                    col = c+dc
                    print('row, m:',row, m)
                    if (row >=0 and row < m) and (col>=0 and col<n):
                        #print(row,col)
                        if (row,col) not in visited and grid[row][col]=='1':
                            q.append((row,col))
                            visited.add((row,col))


        cnt_island = 0
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and grid[i][j]=='1':
                    q = deque()
                    q.append((i,j))
                    bfs(q)
                    cnt_island+=1
        return cnt_island