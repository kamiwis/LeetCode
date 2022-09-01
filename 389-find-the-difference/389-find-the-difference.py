class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for c in t:
            if c not in s or s.count(c) != t.count(c):
                return c
        return -1