class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)

        dp = [[False] * n for _ in range(n)]

        res = s[0]
        max_len = 1

        for l in range(n-1, -1, -1):
            for r in range(l, n):
                if s[l] == s[r] and (r-l <= 2 or dp[l+1][r-1]):
                    dp[l][r] = True

                    if r - l + 1 > max_len:
                        max_len = r - l + 1
                        res = s[l:r + 1]
        return res

                
        