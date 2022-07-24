class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # s = "y#fo##f"
        # t = "y#f#o##f"
        
        ss = []
        ts = []
        
        for i in s:
            if i == '#':
                if ss:
                    ss.pop()
            else:
                ss.append(i)
                
        for i in t:
            if i == '#':
                if ts:
                    ts.pop()
            else:
                ts.append(i)
           
        # print(ss)
        # print(ts)
        return ss == ts