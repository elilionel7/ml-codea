class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd = Counter(s)
        td = Counter(t)
        return sd == td