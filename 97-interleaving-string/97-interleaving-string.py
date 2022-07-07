class Solution(object):
    """def isInterleave(self, s1, s2, s3):

        if len(s3) != len(s1) + len(s2) :
            return False 

        last  = set()  # ((i,j) , (i2,j2))  
        last.add((-1,-1))

        for i in range(len(s3)):   # cal f(i) 
            tmp = set()
            for (m,n) in last :   #(i,j)
                if m+1 <len(s1) and s3[i] == s1[m+1]:
                    tmp.add((m+1,n))
                if n+1 <len(s2) and s3[i] == s2[n+1]:
                    tmp.add((m,n+1))
            last = tmp
            if not last:
                return False

        return True"""

    def isInterleave(self, s1, s2, s3):
        r, c, l= len(s1), len(s2), len(s3)
        if r+c != l:
            return False
        stack, visited = [(0, 0)], set((0, 0))
        while stack:
            x, y = stack.pop()
            if x+y == l:
                return True
            if x+1 <= r and s1[x] == s3[x+y] and (x+1, y) not in visited:
                stack.append((x+1, y)); visited.add((x+1, y))
            if y+1 <= c and s2[y] == s3[x+y] and (x, y+1) not in visited:
                stack.append((x, y+1)); visited.add((x, y+1))
        return False
                    