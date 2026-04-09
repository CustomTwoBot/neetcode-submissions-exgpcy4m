class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashsetS = collections.Counter(s)
        hashsetT = collections.Counter(t)
        if hashsetS != hashsetT:
            return False
        return True