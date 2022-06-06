class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        flag = True
        w = strs[0]
        while(flag):
            flag = False
            for word in strs[1:]:
                # print(word.index(w))
                try:
                    # print(word.index(w))
                    ind = word.index(w)
                    if ind != 0:
                        1/0
                except:
                    if len(w) > 0:
                        w = w[:-1]
                        flag = True
        return w
            