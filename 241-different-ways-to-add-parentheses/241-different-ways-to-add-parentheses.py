class Solution:
    def diffWaysToCompute(self, expression: str, memo = {}) -> List[int]:
        if expression.isdigit():
            return [int(expression)]
        
        if expression in memo:
            return memo[expression]
        
        res = []
        
        for i in range(len(expression)):
            if expression[i] in '-+*':
                res1 = self.diffWaysToCompute(expression[:i])
                res2 = self.diffWaysToCompute(expression[i+1:])
                
                for z in res1:
                    for j in res2:
                        res.append(self.helper(z,j,expression[i]))
                    
            memo[expression] = res
        return res
                    
    def helper(self,i,j,o):
        if o == "+":
            return i + j
        elif o == '-':
            return i - j
        else:
            return i*j