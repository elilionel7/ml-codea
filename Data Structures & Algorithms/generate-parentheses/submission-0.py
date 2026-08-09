class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        pt = []

        def dfs(o,c):
            if o == c == n:
                res.append("".join(pt))
                return
            
            if o < n:
                pt.append('(')
                dfs(o + 1, c)
                pt.pop()
            
            if c < o:
                pt.append(')')
                dfs(o, c + 1)
                pt.pop()
        dfs(0,0)
        return res
            

        