class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        res = ''
        for i in range(0, len(indices)):
            res += s[indices.index(i)]
        return res