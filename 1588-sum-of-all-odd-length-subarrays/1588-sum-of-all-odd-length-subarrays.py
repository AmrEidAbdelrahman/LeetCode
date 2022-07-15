class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = 0
        l = 1
        while l <= len(arr):
            for i in range(0, len(arr)-(l-1)):
                res += sum(arr[i:i+l])
            l += 2
        
        return res