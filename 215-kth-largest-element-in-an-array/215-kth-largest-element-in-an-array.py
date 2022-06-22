
"""class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        que = []
        
        for i in nums:
            heapq.heappush(que,i)
            if len(que) > k:
                heapq.heappop(que)
                
        return heapq.heappop(que)"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """n = len(nums)
        k = n-k 
        def quickSelect(l,r): 
            pivot = nums[r] 
            i = l 
            for j in range(l,r): 
                if nums[j]<=pivot: 
                    nums[i],nums[j]=nums[j],nums[i]
                    i+=1 
            nums[i],nums[r]=nums[r],nums[i] 
            if i>k: return quickSelect(l,i-1)
            elif i<k: return quickSelect(i+1,r)
            else:
                return nums[i]
        return quickSelect(0,n-1)"""
            
        nums.sort()
        return nums[len(nums)-k]