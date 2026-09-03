class Solution:
    def uniquePaths(self, m, n):
        ans = 1

        for i in range(1, n):
            ans = ans * (m + i - 1) // i

        return ans