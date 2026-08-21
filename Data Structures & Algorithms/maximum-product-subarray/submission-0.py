class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = nums[0]
        cur_min = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            
            p_max = cur_max
            p_min = cur_min

            cur_max = max(num, num*p_max, num*p_min)

            cur_min = min(num, num*p_max, num*p_min)

            res = max(res, cur_max)
        
        return res
        