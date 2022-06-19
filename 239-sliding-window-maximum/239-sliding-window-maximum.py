class MyQueue:
    def __init__(self):
        self.queue = []
        
    def pop(self, val):
        if self.queue and val == self.queue[0]:
            self.queue.pop(0)
            
    def push(self,val):
        while self.queue and val > self.queue[-1]:
            self.queue.pop()
        self.queue.append(val)
        
    def front(self):
        return self.queue[0]



class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        myq = MyQueue()
        result = []
        for i in range(k):
            myq.push(nums[i])
            
        result.append(myq.front())
        
        for i in range(k, len(nums)):
            myq.pop(nums[i - k])
            myq.push(nums[i])
            result.append(myq.front())
        
        return result