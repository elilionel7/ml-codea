class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd = {}
        td = {}

        for c in s:
            if c in sd:
                sd[c] += 1
            else:
                sd[c] = 1
        for c in t:
            if c in td:
                td[c] += 1
            else:
                td[c] = 1
        
        return sd == td

        