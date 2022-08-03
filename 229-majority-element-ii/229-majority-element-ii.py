# class Solution:
#     def majorityElement(self, nums: List[int]) -> List[int]:
#         c = Counter()
        
        
#         for i in nums:
#             c[i] += 1
#             if len(c) == 3:
#                 nc = Counter()
#                 for j, v in c.items():
#                     if v != 1:
#                         nc[j] = v - 1   
#                 c = nc
                
#         pool = Counter ( n for n in nums if n in c)
        
#         return [n for n in pool if pool[n] > len(nums)//3]


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        lst=[]
        for i in count:
            if count[i]>(len(nums)//3):
                lst.append(i)
        return lst