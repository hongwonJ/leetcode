class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        if (coordinates[0][0] == coordinates[1][0]): m = float(inf)
        else: m = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
        
        for i in range(2, len(coordinates)):
            if (coordinates[i][0] == coordinates[i-1][0]): 
                if m != float(inf): return False
            elif (coordinates[i][1] - coordinates[i-1][1]) / (coordinates[i][0] - coordinates[i-1][0]) != m:
                return False
        return True
            
            