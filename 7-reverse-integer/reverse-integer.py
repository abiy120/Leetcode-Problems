class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            negative = True
            x = abs(x)
        res = int(str(x)[::-1])
        if negative:
            res -= 2 * res
        if res > (2**31 - 1) or res < (-(2**31)):
            return 0
        else:
            return res