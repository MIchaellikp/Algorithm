"""class Solution:
     def longestCommonPrefix(self, strs):

            if not strs:
                return ""
            shortest = min(strs,key=len)
            for i, ch in enumerate(shortest):
                for other in strs:
                    if other[i] != ch:
                        return shortest[:i]
            return shortest""" 
            
class Solution(object):
    def longestCommonPrefix(self, strs):
        result = ""       
        for n in zip(*strs):
            if len(set(n)) == 1:
                result += n[0]
            else:
                return result
        return result