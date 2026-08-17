class Solution(object):
    def romanToInt(self, s):
        ans = 0
        prev = 0
        i = len(s) - 1

        while i >= 0:
            c = s[i]

            if c == 'I':
                v = 1
            elif c == 'V':
                v = 5
            elif c == 'X':
                v = 10
            elif c == 'L':
                v = 50
            elif c == 'C':
                v = 100
            elif c == 'D':
                v = 500
            else:
                v = 1000

            if v < prev:
                ans -= v
            else:
                ans += v

            prev = v
            i -= 1

        return ans