class Solution(object):
    def myAtoi(self, s):
        i = 0
        n = len(s)

        # 1. Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # 2. Check sign
        sign = 1

        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1

        # 3. Convert digits
        result = 0

        while i < n and s[i].isdigit():
            digit = int(s[i])

            # 4. Check overflow before adding digit
            if result > (2**31 - 1 - digit) // 10:
                if sign == 1:
                    return 2**31 - 1
                else:
                    return -2**31

            result = result * 10 + digit
            i += 1

        return sign * result