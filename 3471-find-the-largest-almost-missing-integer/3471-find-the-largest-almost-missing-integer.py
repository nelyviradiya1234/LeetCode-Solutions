class Solution:
    def largestInteger(self, nums, k):
        n = len(nums)

        if k > n:
            return -1

        first = {}
        last = {}

        for i, x in enumerate(nums):
            if x not in first:
                first[x] = i
            last[x] = i

        max_start = n - k
        answer = -1

        for x in first:
            left = max(0, first[x] - k + 1)
            right = min(max_start, last[x])

            if left == right:
                answer = max(answer, x)

        return answer