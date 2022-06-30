class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        res = 0
        j = [jewels[i] for i in range(0, len(jewels))]
        i = 0
        for i in range(0,len(stones)):
            if stones[i] in j:
                res += 1
        return res
        