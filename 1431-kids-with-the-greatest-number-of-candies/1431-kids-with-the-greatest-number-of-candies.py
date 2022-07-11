class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        res = []
        maxi = max(candies)
        for i in range(0,len(candies)):
            res.append(candies[i] + extraCandies >=maxi)
            
        return res
        