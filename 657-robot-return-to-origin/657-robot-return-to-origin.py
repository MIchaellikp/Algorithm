class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0
        y = 0
        
        for i in range(len(moves)):
            if moves[i] == 'U':
                x += 1
            elif moves[i] == 'D':
                x -= 1
            elif moves[i] == 'L':
                y += 1
            elif moves[i] == 'R':
                y -= 1
        return x==0 and y ==0
                 