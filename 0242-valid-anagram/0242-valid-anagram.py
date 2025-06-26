class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap1 = {}
        hmap2 = {}
        for char1 in s:
            if char1 in hmap1:
                hmap1[char1] += 1
            else:
                hmap1[char1] = 1

        for char2 in t:
            if char2 in hmap2:
                hmap2[char2] += 1
            else:
                hmap2[char2] = 1
        if hmap1 == hmap2:
            return True
        else:
            return False
            