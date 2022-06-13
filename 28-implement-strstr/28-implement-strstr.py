class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        for i in range(0, len(haystack)):
            if (needle == haystack[i:i+len(needle)]):
                return i
        return -1
        