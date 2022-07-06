class Solution(object):
    def tribonacci(self, n, memo={}):
        """
        :type n: int
        :rtype: int
        """
        if n in memo:
            return memo[n]
        if n < 2:
            return n
        if n == 2:
            return 1
        memo[n] = self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)
        return memo[n]