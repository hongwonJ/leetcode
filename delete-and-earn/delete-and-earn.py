class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        num_dic = {}
        for num in sorted(nums):
            if num in num_dic: num_dic[num] += 1
            else: num_dic[num] = 1
        
        n = len(num_dic)
        ans = []
        max_ = 0 
        
        for k,v in num_dic.items():
            if len(ans) == 0:
                ans.append(k*v)
            elif len(ans) == 1:
                ans.append(k*v)
                if k-1 not in num_dic: ans[-1] += ans[-2]
            else:
                if ans[-2] > max_: max_ = ans[-2]
                if k-1 not in num_dic: ans.append(max(max_, ans[-1]) + k*v)
                else: ans.append(max_ + k*v)
        return max(ans)
            