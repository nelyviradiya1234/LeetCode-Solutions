class Solution:
    def getPermutation(self, n, k):
        nums = [str(i) for i in range(1, n + 1)]
        result = []

        k -= 1

        factorial = 1
        for i in range(1, n):
            factorial *= i

        for remaining in range(n, 0, -1):
            index = k // factorial
            result.append(nums.pop(index))

            if remaining > 1:
                k %= factorial
                factorial //= (remaining - 1)

        return ''.join(result)