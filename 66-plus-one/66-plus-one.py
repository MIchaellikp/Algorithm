class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        hold  = 1
        
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:
                digits[i] = digits[i] + hold
                return digits
            else:
                digits[i] = 0
                
        digits.insert(0,1)
        
        return digits