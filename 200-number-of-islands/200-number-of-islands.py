class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def helper(i,j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
                return 

            grid[i][j] = '.'
            helper(i + 1, j)
            helper(i - 1, j)
            helper(i, j + 1)
            helper(i, j - 1)
            
            
        if not grid:
            return 0
            
        res = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res += 1
                    helper(i,j)
                    
        return res