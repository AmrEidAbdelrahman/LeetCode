class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # nums_len = len(nums)
        # res = [0 for i in range(0, nums_len*2)]
        # for i in range(0, nums_len):
        #     res[i] = nums[i]
        #     res[nums_len+i] = nums[i]
        # return res
        return nums * 2