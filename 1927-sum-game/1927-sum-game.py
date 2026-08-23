class Solution:
    def sumGame(self, num):
        n = len(num)
        half = n // 2

        diff = 0
        q = 0

        for i in range(n):
            if num[i] == '?':
                if i < half:
                    q += 1
                else:
                    q -= 1
            else:
                if i < half:
                    diff += int(num[i])
                else:
                    diff -= int(num[i])

        return diff * 2 + q * 9 != 0