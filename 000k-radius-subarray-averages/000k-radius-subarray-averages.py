class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        p_sum = nums.copy()
        prev_num = 0
        for i in range(len(p_sum)):
            p_sum[i] += prev_num
            prev_num = p_sum[i]
        averages = []
        tot = -1
        for i in range(len(p_sum)):
            l, r = i - k - 1, i + k
            if l + 1 < 0 or r >= len(p_sum):
                averages.append(-1)
            elif l == -1:
                averages.append((p_sum[r])//(2*k+1))
            else:
                averages.append((p_sum[r]-p_sum[l])//(2*k+1))
        return averages
            




            