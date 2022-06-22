
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        que = []
        
        for i in nums:
            heapq.heappush(que,i)
            if len(que) > k:
                heapq.heappop(que)
                
        return heapq.heappop(que)