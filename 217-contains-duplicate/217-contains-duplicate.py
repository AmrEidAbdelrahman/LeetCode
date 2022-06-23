class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # visited = []
        # for i in nums:
        #     if i in visited:
        #         return True
        #     visited.append(i)
    
        # return False
        
        return len(nums) != len(set(nums))