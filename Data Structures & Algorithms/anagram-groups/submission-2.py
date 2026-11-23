class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        res = []

        for i in strs:
            stringsAscending = "".join(sorted(i))

            if stringsAscending not in hashmap:
                hashmap[stringsAscending] = [i]
            else:
                hashmap[stringsAscending].append(i)

        return list(hashmap.values())

        

            
            
            
        