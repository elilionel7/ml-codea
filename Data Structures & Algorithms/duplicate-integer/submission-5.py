class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        seen = 0
        mn = min(nums)
        for n in nums:
            n = n - mn #offset n so theres no negative number
            mask = 1 << n

            if seen & mask:
                return True
            seen |= mask
        
        return False
        