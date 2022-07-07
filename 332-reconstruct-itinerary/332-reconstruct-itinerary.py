"""class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        d = defaultdict(list)
        path = ['JFK']
        
        for item in tickets:
            d[item[0]].append(item[1])
            
            
        def helper(s):
            if len(path) == len(tickets) + 1:
                return True
            
            d[s].sort()
            
            for _ in d[s]:
                end = d[s].pop(0)
                path.append(end)
                if helper(end):
                    return True
                path.pop()
                d[s].append(end)
                
                
        helper('JFK')
        
        return path"""

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        tickets.sort()
        
        graph = defaultdict(list)
        
        for i, (f, t) in enumerate(tickets):
            graph[f].append((t, i))
            
        visited = set()
        
        def dfs(curr):
            if len(curr) == len(tickets) + 1:
                return True
            
            for t, i in graph[curr[-1]]:
                if i in visited:
                    continue
                
                visited.add(i)
                
                curr.append(t)
                
                if dfs(curr):
                    return True

                curr.pop()
                
                visited.remove(i)
            
            return False
        
        curr = ['JFK']
        
        for t, i in graph['JFK']:
            visited.add(i)
            
            curr.append(t)
            
            if dfs(curr):
                return curr
            
            curr.pop()
            
            visited.remove(i)
        