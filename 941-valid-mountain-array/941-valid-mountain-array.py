class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        n = len(arr)
        l = 0
        r = n - 1
        
        while l < n - 1 and arr[l] < arr[l+1]:
                l += 1
                
        while r > 1 and arr[r] < arr[r - 1]:
            r -= 1
            
        return l == r and r != 0 and l != n-1
            
        
                
                
        
        