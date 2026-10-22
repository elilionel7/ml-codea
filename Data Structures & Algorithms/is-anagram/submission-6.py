class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ars = [0] * 26
        

        for i in range(len(s)):
            ars[ord(s[i])-ord("a")] += 1
            ars[ord(t[i])-ord("a")] -= 1
        for n in ars:
            if n != 0:
                return False
        return True
        

        
        

