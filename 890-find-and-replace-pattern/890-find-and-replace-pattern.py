class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        
        for i in words:
            d1, d2 = {}, {}
            flag = True
            for j in range(len(i)):
                if i[j] not in d1:
                    d1[i[j]] = pattern[j]
                if pattern[j] not in d2:
                    d2[pattern[j]] = i[j]
                    
                if (d1[i[j]], d2[pattern[j]]) != (pattern[j], i[j]):
                    flag = False
                    break
            if flag:
                res.append(i)
                
        return res