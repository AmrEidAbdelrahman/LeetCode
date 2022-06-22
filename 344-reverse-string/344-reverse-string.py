class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # return s.reverse()
        l = len(s)-1
        mid = len(s)//2
        for i in range(0, mid):
            cub = s[l-i]
            s[l-i] = s[i]
            s[i] = cub
        return s