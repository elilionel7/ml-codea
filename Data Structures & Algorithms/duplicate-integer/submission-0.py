class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ch = set()

        for n in nums:
            if n in ch:
                return True
            ch.add(n)
        return False
        