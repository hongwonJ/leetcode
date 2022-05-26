class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rst = []
        for i in range(1, numRows + 1):
            rst.append([])
            for j in range(1, i + 1):
                if i < 3: rst[i - 1].append(1)
                else:
                    if j == 1 or j == i:
                        rst[i - 1].append(1)
                    else:
                        rst[i - 1].append(rst[i - 2][j - 2] + rst[i - 2][j - 1])
        return rst