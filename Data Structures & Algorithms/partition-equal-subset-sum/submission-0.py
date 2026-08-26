class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)

        if tot % 2 != 0:
            return False
        
        target = tot // 2

        dp = [False] * (target + 1)
        dp[0] = True #we can make a sum of zero by choosing nothing

        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        
        return dp[target]

        