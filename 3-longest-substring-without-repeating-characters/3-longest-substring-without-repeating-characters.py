class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #slide window
        
        d = {}
        start = 0
        longest = 0
        if len(s) <= 1:
            return len(s)
        
        for i in range(len(s)):
            if s[i] in d and start<= d[s[i]]:
                start = d[s[i]] + 1
            else:
                longest = max(longest, i - start + 1)

            d[s[i]] = i
                
               
        return longest