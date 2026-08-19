class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        rows = {}

        for row, seat in reservedSeats:
            rows[row] = rows.get(row, 0) | (1 << seat)

        answer = 2 * n

        left = (1 << 2) | (1 << 3) | (1 << 4) | (1 << 5)
        middle = (1 << 4) | (1 << 5) | (1 << 6) | (1 << 7)
        right = (1 << 6) | (1 << 7) | (1 << 8) | (1 << 9)

        for mask in rows.values():
            if (mask & left) == 0 and (mask & right) == 0:
                continue
            elif (mask & left) == 0 or (mask & middle) == 0 or (mask & right) == 0:
                answer -= 1
            else:
                answer -= 2

        return answer