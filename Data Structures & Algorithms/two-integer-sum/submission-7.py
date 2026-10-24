class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = [(i, num) for i, num in enumerate(nums)]
        arr.sort(key=lambda x: x[1])

        l, r = 0, len(arr) - 1

        while l < r:
            total = arr[l][1] + arr[r][1]

            if total == target:
                return sorted([arr[l][0], arr[r][0]])
            elif total > target:
                r -= 1
            else:
                l += 1