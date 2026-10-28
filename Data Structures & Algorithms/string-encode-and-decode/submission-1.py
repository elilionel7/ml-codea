class Solution:

    def encode(self, strs: list[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            # Find the '#'
            while s[j] != "#":
                j += 1

            # Everything from i to j is the length
            length = int(s[i:j])

            # The actual string starts after '#'
            start = j + 1
            end = start + length

            res.append(s[start:end])

            # Move i to the next encoded string
            i = end

        return res