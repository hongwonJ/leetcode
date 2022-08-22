class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        horBool = all([self.findDuplicate(hor) for hor in board])
        
        vers = []
        for i in range(9):
            ver = []
            for j in range(9):
                ver.append(board[j][i])
            vers.append(ver)
        
        verBool = all([self.findDuplicate(hor) for hor in vers])
        
        blocks = [[] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                blocks[(i//3)*3 + j//3].append(board[i][j])
        bloBool = all([self.findDuplicate(blo) for blo in blocks])
        
        return horBool and verBool and bloBool
    
    def findDuplicate(self, line)-> bool:
        dupSet = set()
        dupList = []
        for num in line:
            if num != ".":
                dupSet.add(num)
                dupList.append(num)
        n, m = len(dupSet), len(dupList)
        return True if n == m else False
      
    