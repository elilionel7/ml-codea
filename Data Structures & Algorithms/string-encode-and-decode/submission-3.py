from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for s in strs:
            res.append(str(len(s)) + "#" + s)

        return "".join(res)


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            # Find where the length ends
            while s[j] != "#":
                j += 1

            # Get the length of the string
            length = int(s[i:j])

            # The actual string starts after #
            start = j + 1
            end = start + length

            res.append(s[start:end])

            # Move to the next encoded string
            i = end

        return res