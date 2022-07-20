class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []
        parte = ['(', ')']
        def helper(path, l , r):
            if len(path) == n*2:
                res.append(''.join(path))
            
            if l < n:
                path.append('(')
                helper(path,l+1, r)
                path.pop()
                
            if r < l:
                path.append(')')
                helper(path, l ,r + 1)
                path.pop()
                
                
        helper(path,0,0)
        return res