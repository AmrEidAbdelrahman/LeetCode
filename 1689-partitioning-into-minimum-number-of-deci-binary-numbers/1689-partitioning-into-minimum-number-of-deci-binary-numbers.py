class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        maxi = 0
        for i in range(0, len(n)):
            if n[i] > maxi:
                maxi = n[i]
                
        return maxi