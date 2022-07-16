class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @lru_cache(None)
        def helper(x,y,rm):
            if x >= m or y >= n or x < 0 or y < 0:
                return 1
            if rm <= 0:
                return 0

            a = helper(x-1, y, rm - 1)
            b = helper(x+1, y, rm - 1)
            c = helper(x, y-1, rm - 1)
            d = helper(x, y+1, rm - 1)
                
            return a + b + c + d
        
        return helper(startRow,startColumn, maxMove)% 1_000_000_007
            
            
            