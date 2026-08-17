class Solution(object):
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)

        if n <= 1:
            return 0

        # Prefix sums
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        # dp[i][j] = maximum score Alice can get
        # from stones i to j
        dp = [[0] * n for _ in range(n)]

        # bestLeft[i][j] =
        # max(dp[i][k] + prefix[k+1]) for k from i to j
        bestLeft = [[0] * n for _ in range(n)]

        # bestRight[i][j] =
        # max(dp[k][j] - prefix[k]) for k from i to j
        bestRight = [[0] * n for _ in range(n)]

        # Initialize ranges containing one stone
        for i in range(n):
            bestLeft[i][i] = prefix[i + 1]
            bestRight[i][i] = -prefix[i]

        # Build DP by increasing length
        for length in range(2, n + 1):

            for left in range(n - length + 1):
                right = left + length - 1

                total = prefix[right + 1] - prefix[left]

                # Find the first split where
                # left_sum >= right_sum
                lo = left
                hi = right - 1

                while lo < hi:
                    mid = (lo + hi) // 2

                    left_sum = prefix[mid + 1] - prefix[left]

                    if 2 * left_sum >= total:
                        hi = mid
                    else:
                        lo = mid + 1

                split = lo

                # If even the last possible left side
                # is smaller than the right side
                if 2 * (prefix[split + 1] - prefix[left]) < total:
                    split = right

                answer = 0

                # Case 1:
                # left side is smaller
                if split == right:
                    last = right - 1
                else:
                    split_left_sum = prefix[split + 1] - prefix[left]

                    # Equal sums: Alice can choose either side
                    if 2 * split_left_sum == total:
                        last = split
                    else:
                        last = split - 1

                if last >= left:
                    answer = max(
                        answer,
                        bestLeft[left][last] - prefix[left]
                    )

                # Case 2:
                # right side is smaller
                if split <= right - 1:
                    answer = max(
                        answer,
                        prefix[right + 1] + bestRight[split + 1][right]
                    )

                dp[left][right] = answer

                # Update bestLeft
                bestLeft[left][right] = max(
                    bestLeft[left][right - 1],
                    dp[left][right] + prefix[right + 1]
                )

                # Update bestRight
                bestRight[left][right] = max(
                    bestRight[left + 1][right],
                    dp[left][right] - prefix[left]
                )

        return dp[0][n - 1]