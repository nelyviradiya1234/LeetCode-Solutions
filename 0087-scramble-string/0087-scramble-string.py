class Solution:
    def isScramble(self, s1, s2):
        n = len(s1)

        if s1 == s2:
            return True

        if sorted(s1) != sorted(s2):
            return False

        dp = [[[False] * (n + 1) for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                dp[i][j][1] = s1[i] == s2[j]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                for j in range(n - length + 1):
                    for k in range(1, length):
                        if (dp[i][j][k] and
                            dp[i + k][j + k][length - k]):
                            dp[i][j][length] = True
                            break

                        if (dp[i][j + length - k][k] and
                            dp[i + k][j][length - k]):
                            dp[i][j][length] = True
                            break

        return dp[0][0][n]