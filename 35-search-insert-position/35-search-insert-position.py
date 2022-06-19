class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        pos = 0
        maxi = float('-inf')
        for i in range(0,len(nums)):
            if nums[i] == target:
                return i
            else:
                if nums[i] < target and nums[i] > maxi:
                    maxi = nums[i]
                    pos = i + 1
            if nums[i] > target:
                return pos
        return pos