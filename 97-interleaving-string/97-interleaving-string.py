class Solution(object):
    def isInterleave(self, s1, s2, s3, memo={}):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if '-'.join(s3)+'|'+'-'.join(s2)+'|'+'-'.join(s1) in memo:
            return memo['-'.join(s3)+'|'+'-'.join(s2)+'|'+'-'.join(s1)]
        if s3 == '':
            if len(s1) == 0 and len(s2) == 0:
                return True
        else:
            if len(s1) > 0 and s3[0] == s1[0] and self.isInterleave(s1[1:], s2, s3[1:], memo):
                memo['-'.join(s3)+'|'+'-'.join(s2)+'|'+'-'.join(s1)] = True
                return True
            if len(s2) > 0 and s3[0] == s2[0] and self.isInterleave(s1, s2[1:], s3[1:], memo):
                memo['-'.join(s3)+'|'+'-'.join(s2)+'|'+'-'.join(s1)] = True
                return True
        memo['-'.join(s3)+'|'+'-'.join(s2)+'|'+'-'.join(s1)] = False
        return False
        