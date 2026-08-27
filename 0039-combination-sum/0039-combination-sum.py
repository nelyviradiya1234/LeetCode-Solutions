class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, remaining, current):
            if remaining == 0:
                result.append(current[:])
                return

            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                num = candidates[i]

                if num > remaining:
                    continue

                current.append(num)

                backtrack(i, remaining - num, current)

                current.pop()

        candidates.sort()
        backtrack(0, target, [])

        return result