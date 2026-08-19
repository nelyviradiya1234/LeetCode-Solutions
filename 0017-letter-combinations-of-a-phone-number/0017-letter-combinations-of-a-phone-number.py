class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []

        phone = [
            "", "", "abc", "def", "ghi",
            "jkl", "mno", "pqrs", "tuv", "wxyz"
        ]

        n = len(digits)
        result = []
        current = [''] * n

        def backtrack(index):
            if index == n:
                result.append(''.join(current))
                return

            for letter in phone[ord(digits[index]) - 48]:
                current[index] = letter
                backtrack(index + 1)

        backtrack(0)
        return result