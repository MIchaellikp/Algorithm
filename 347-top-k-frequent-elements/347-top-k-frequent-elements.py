class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        
        for i in nums:
            d[i] = d.get(i,0) + 1
            
        heap = []
        
        for num, count in d.items():

            ele = (count,num)
            heapq.heappush(heap, ele)
            if len(heap) > k:
                heapq.heappop(heap)
                
        result = [x[1] for x in heap]
        
        return result