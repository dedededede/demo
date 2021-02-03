class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)
        dp = [[False for i in range(n + 1)] for j in range(m + 1)]
        dp[0][0] = True

        for j in range(n):

            dp[0][j + 1] = dp[0][j] and p[j] == '*'

            for i in range(m):

                if p[j] == '*':
                    dp[i + 1][j + 1] = dp[i + 1][j] or dp[i][j] or dp[i][j + 1]
                else:
                    dp[i + 1][j + 1] = dp[i][j] and (p[j] == '?' or p[j] == s[i])

        return dp[m][n]

obj = Solution()
print obj.isMatch('aa', 'a')
