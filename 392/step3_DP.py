class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(s) == 0:
            return True
        
        dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]

        for row in range(1, len(s)+1):
            for column in range(1, len(t)+1):
                if s[row - 1] == t[column - 1]:
                    dp[row][column] = dp[row-1][column-1] + 1
                else:
                    dp[row][column] = max(dp[row][column-1], dp[row-1][column])
        
        if len(s) == dp[-1][-1]:
            return True
        
        return False
