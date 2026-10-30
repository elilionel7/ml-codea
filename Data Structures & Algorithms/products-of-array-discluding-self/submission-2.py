class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [1] * n
        posf = [1] * n
        #[1,1,2,8]
        #[48,24,6,1] [1,1,1,1]
        for i in range(1,n):
            pref[i] = pref[i-1] * nums[i-1]
        
        for i in range(n-2, -1, -1):
            
            posf[i] = posf[i+1] * nums[i+1]
        
        for i in range(n):
            pref[i] *= posf[i]
        
        return pref

