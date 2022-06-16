class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict_, stack = {}, []
        ans = []
        for n in nums2:
            if not stack: stack.append(n)
            if stack[-1] > n:
                stack.append(n)
            else:
                while stack and stack[-1] < n:
                    dict_[stack.pop()] = n
            stack.append(n)
        
        for n in nums1:
            if n in dict_: ans.append(dict_[n])
            else: ans.append(-1)
        
        return ans