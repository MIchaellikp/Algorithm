class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        conncted = defaultdict(list)
        for e in edges:
            visited = defaultdict(bool)
            x, y = e[0], e[1]
            if self.isconnected(x,y,conncted,visited):
                return e
            conncted[x].append(y)
            conncted[y].append(x)
            
    def isconnected(self,x,y,conncted,visited):
        if x == y:
            return True
        
        for xc in conncted[x]:
            if not visited[xc]:
                visited[xc] = True
                if self.isconnected(xc,y,conncted, visited):
                    return True
        return False
                

                
                
# class Solution:
#     def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
#         self.already_connected = defaultdict(list)
#         for edge in edges:
#             self.visited = defaultdict(bool)
#             x, y = edge[0], edge[1]
#             if self.is_already_connected(x, y):
#                 return edge
#             self.already_connected[x].append(y)
#             self.already_connected[y].append(x)
            
#     def is_already_connected(self, x, y):
#         if x == y:
#             return True
#         for x_adjacent in self.already_connected[x]:
#             if not self.visited[x_adjacent]:
#                 self.visited[x_adjacent] = True
#                 if self.is_already_connected(x_adjacent, y):
#                     return True
#         return False