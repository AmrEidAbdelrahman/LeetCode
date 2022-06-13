class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        res = next((i for i in range(0, len(haystack) - len(needle) + 1) if needle == haystack[i:i+len(needle)]), -1)
        return res
        # for i in range(0, len(haystack)):
        #     if (needle == haystack[i:i+len(needle)]):
        #         return i
        # return -1
        