class Solution:

    def encode(self, strs: List[str]) -> str:
        finalString = ""
        for i in strs:
            finalString += str(len(i)) + "#" + i
        return finalString

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res
        
