class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(0, len(nums)):
            curr = 0
            for j in range(0, len(nums)):
                if nums[j] < nums[i]:
                    curr += 1
            res.append(curr)
            
        return res
        