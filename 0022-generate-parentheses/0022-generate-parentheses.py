class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dt = [None for _ in range(n+1)]
        return self.buildNpar(n, dt)    
            
    def buildNpar(self, n, dt):
        if dt[n] is not None: return dt[n]
        if n == 1: ans = ["()"]
        else:
            ans = []
            out_pars = self.buildNpar(n-1, dt)
            for out_par in out_pars:
                ans.append("()"+out_par)
                ans.append("("+out_par+")")
            for i in range(1, n-1):
                in_pars = self.buildNpar(i, dt)
                out_pars = self.buildNpar(n-1-i, dt)
                for in_par in in_pars:
                    for out_par in out_pars:
                        ans.append("(" + in_par + ")" + out_par)
        dt[n] = ans
        return ans