class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []

        def backtrack(start, remaining, current):
            if remaining == 0:
                result.append(current[:])
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] > remaining:
                    break

                current.append(candidates[i])

                backtrack(i + 1, remaining - candidates[i], current)

                current.pop()

        backtrack(0, target, [])
        return result