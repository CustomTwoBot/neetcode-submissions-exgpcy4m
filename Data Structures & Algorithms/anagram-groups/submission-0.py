class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {} # key : strings
        anagramList = []
        for i in strs:
            count = [0] * 26 # initialize count variable with 26 zeroes
            for j in i:
                count[ord(j) - ord("a")] += 1
            if tuple(count) not in hashmap:
                hashmap[tuple(count)] = [i]
            else:
                hashmap[tuple(count)].append(i)
        return list(hashmap.values())
        

            
            
            
        