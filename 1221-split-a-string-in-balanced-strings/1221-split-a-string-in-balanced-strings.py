class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balence = 0
        count = 0
        for i in range(len(s)):
            if(s[i] == 'L'):
                balence += 1
            else:
                balence -= 1
            
            if(balence == 0):
                count += 1
        
        return count