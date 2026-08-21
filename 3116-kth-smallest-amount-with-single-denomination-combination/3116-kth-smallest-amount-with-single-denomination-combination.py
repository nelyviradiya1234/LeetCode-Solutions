class Solution:
    def findKthSmallest(self, coins, k):
        n = len(coins)

        def count(x):
            total = 0

            for mask in range(1, 1 << n):
                lcm = 1
                bits = 0
                valid = True

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1

                        g = self.gcd(lcm, coins[i])
                        lcm = lcm // g * coins[i]

                        if lcm > x:
                            valid = False
                            break

                if not valid:
                    continue

                if bits % 2 == 1:
                    total += x // lcm
                else:
                    total -= x // lcm

            return total

        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a