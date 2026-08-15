class Solution(object):
    def longestPalindrome(self, s):
        if not s:
            return ""

        start = 0
        end = 0

        for i in range(len(s)):
            # Odd length palindrome
            len1 = self.expand(s, i, i)

            # Even length palindrome
            len2 = self.expand(s, i, i + 1)

            length = max(len1, len2)

            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2

        return s[start:end + 1]

    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return right - left - 1