class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)

        reversed_num = 0

        while x > 0:
            digit = x % 10
            x //= 10

            # Check overflow before multiplying by 10
            if reversed_num > (2**31 - 1 - digit) // 10:
                return 0

            reversed_num = reversed_num * 10 + digit

        return sign * reversed_num