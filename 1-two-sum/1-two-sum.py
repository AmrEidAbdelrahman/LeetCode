class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for counter, num in enumerate(nums):
            second = target - num
            index_of_second = nums.index(second) if second in nums else -1
            if index_of_second != -1 and counter != index_of_second:
                return [counter, index_of_second]