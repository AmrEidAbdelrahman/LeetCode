class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        maxi = 0
        for i in range(0, len(accounts)):
            res = sum(accounts[i])
            if res > maxi:
                maxi = res
        return maxi