class Solution:
    hashmap = {}
    def encode(self, strs: List[str]) -> str:
        string = ""
        for i in strs:
            string += i + ";;"

        self.hashmap[string] = strs
        return string
    def decode(self, s: str) -> List[str]:
        return self.hashmap[s]
