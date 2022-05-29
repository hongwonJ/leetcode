class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box = self.boxCon(board)
        for row in board:
            for i in range(9):
                if row[i].isdigit() and row[i] in row[i + 1:]: return False
        for col in zip(*board):
            for i in range(9):
                if col[i].isdigit() and col[i] in col[i + 1:]: return False
        for ln in box:
            for i in range(9):
                if ln[i].isdigit() and ln[i] in ln[i + 1:]: return False
        return True
        
                        
                
    def boxCon(self, board: List[List[str]]) -> List[List[str]]:
        box = []
        for i in range(3):
            for j in range(3):
                box.append([])
                for k in range(3): box[3 * i + j] += board[3 * i + k][j * 3: j * 3 + 3]
        return box