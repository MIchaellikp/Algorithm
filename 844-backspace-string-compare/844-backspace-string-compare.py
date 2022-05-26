class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        newS = []
        newT = []
        temp = 0
        sL = len(s) - 1
        tL = len(t) - 1
        while sL >= 0:
            if s[sL] == '#':
                temp += 1
            else:
                if temp > 0:
                    temp -= 1
                else:
                    newS.insert(0, s[sL])
            sL -= 1
            
        temp = 0       
        while tL >= 0:
            if t[tL] == '#':
                temp += 1
            else:
                if temp > 0:
                        temp -= 1
                else:
                    newT.insert(0, t[tL])
            tL -= 1
                 
        return newS == newT
        
                