class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A  

        total = len(A) + len(B)
        half = (total + 1) // 2  
        l, r = 0, len(A)         

        while True:
            i = (l + r) // 2         # elements from A
            j = half - i             # elements from B

            # boundaries
            Aleft = A[i-1] if i > 0 else -10**7   # use -inf conceptually
            Aright = A[i] if i < len(A) else 10**7
            Bleft = B[j-1] if j > 0 else -10**7
            Bright = B[j] if j < len(B) else 10**7

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 1:
                    return max(Aleft, Bleft)   # left half has one extra
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1   # too many from A, reduce
            else:
                l = i + 1   # too few from A, increase