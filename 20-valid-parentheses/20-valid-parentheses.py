class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        
        for i in s:
            if i == "(":
                stack.append(")")
            elif i == '[':
                stack.append(']')
            elif i == '{':
                stack.append('}')
            else:
                if not stack or i != stack.pop():
                    return False
                
                
        return True if not stack else False