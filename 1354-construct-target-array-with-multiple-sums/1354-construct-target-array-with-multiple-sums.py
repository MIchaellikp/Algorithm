class Solution:
    def isPossible(self, A):
        total = sum(A)
        A = [-a for a in A]
        heapq.heapify(A)
        while True:
            a = -heapq.heappop(A)
            #print(a)
            total -= a
            if a == 1 or total == 1: return True
            if a < total or total == 0 or a % total == 0:
                return False
            a %= total
            #print(a)
            total += a
            heapq.heappush(A, -a)
            #print(A)