class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = 0
        prod = 1
        n = str(n)
        for i in range(0, len(n)):
            s += int(n[i])
            prod *= int(n[i])
            
        return prod - s
        