class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(n, l, r):
            while l < r:
                n[l], n[r] = n[r], n[l]
                l += 1
                r -= 1
            
            return n
        
        l = len(nums)
        k = k % l
        
        reverse(nums, 0, l - 1)
        reverse(nums, 0 , k - 1)
        reverse(nums, k , l - 1)