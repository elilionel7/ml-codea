class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        dig_let = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
        }

        res = []
        comb = []

        def  dfs(i):
            if i == len(digits):
                res.append(''.join(comb))
                return



            for e in dig_let[digits[i]]:
                comb.append(e)
                
                dfs(i+1)

                comb.pop()



        dfs(0)
        return res
        