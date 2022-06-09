class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(s) < len(p):
            return []
        
        slow = 0
        fast = 0
        hmap = [0] * 26
        cmap = [0] * 26
        
        for i in p:
            cmap[ord(i) - ord('a')] += 1
        
        result = []
        while fast < len(s):
            while fast - slow < len(p):
                if s[fast] in p:
                    hmap[ord(s[fast]) - ord('a')] += 1
                fast += 1
            if hmap == cmap:
                result.append(slow)
            if s[slow] in p:
                hmap[ord(s[slow]) - ord('a')] -= 1
            slow += 1
            


            
        return result
                
            
                
            