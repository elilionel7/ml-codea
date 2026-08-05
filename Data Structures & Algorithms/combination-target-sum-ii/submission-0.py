class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        com = []
        candidates.sort()

        def dfs(i, cursum):
            if cursum == target:
                res.append(com.copy())
                return
            if cursum > target or i == len(candidates):
                return
            
            com.append(candidates[i])

            dfs(i+1, cursum + candidates[i])
            com.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, cursum)
        
        dfs(0,0)
        return res

        