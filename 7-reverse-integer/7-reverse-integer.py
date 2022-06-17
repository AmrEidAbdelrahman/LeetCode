class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            res = int(str(x)[::-1])
        elif x < 0:
            val = str(x)[1:]
            res = 0 - int(val[::-1])
        else:
            res = x
        if res < -2**31 or res > (2**31) - 1:
            return 0
        return res