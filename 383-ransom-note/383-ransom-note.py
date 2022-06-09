class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        hm = [0] * 26
        
        for i in magazine:
            hm[ord(i) - ord('a')] += 1
            
        for j in ransomNote:
            hm[ord(j) - ord('a')] -= 1
            
            
        for i in hm:
            if i < 0:
                return False
                break
        return True