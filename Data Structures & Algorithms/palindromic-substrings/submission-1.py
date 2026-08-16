class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        dp = [[False] * n for _ in range(n)]
        palindromeCount = 0

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i + 1 <= 2 or dp[i+1][j-1] == True):
                    dp[i][j] = True
                    palindromeCount += 1
        
        return palindromeCount