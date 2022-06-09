class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashtable = [0] * 26
        
        for i in s:
            hashtable[ord(i) - ord('a')] += 1
            
        for i in t:
            hashtable[ord(i) - ord('a')] -= 1
            
        for j in hashtable:
            if j != 0:
                return False
                break
        return True
        