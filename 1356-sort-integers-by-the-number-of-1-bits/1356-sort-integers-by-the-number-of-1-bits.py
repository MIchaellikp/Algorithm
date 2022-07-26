class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key = lambda x: (self.c(x),x))
        return arr
    
    
    def c(self, num):
        co = 0
        
        while num:
            num &= num - 1
            co += 1
            
        return co
        
        
        