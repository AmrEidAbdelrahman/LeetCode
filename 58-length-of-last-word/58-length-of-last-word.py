class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.rstrip()
        arr = s.split(' ')
        last = arr[-1]
        return len(last)
        