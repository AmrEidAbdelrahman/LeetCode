class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i in range(0, n):
            res.append(nums[i])
            res.append(nums[i+n])
        return res