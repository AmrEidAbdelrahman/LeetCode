class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        maxi = 0
        words = []
        for sentence in sentences:
            words = sentence.split(' ')
            maxi = max(maxi, len(words))
        return maxi
        