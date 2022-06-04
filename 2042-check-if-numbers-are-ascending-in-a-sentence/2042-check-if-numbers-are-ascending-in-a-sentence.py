class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        list_of_words = s.split(' ')
        old = -10000
        for word in list_of_words:
            if word.isnumeric():
                if int(word) > old:
                    old = int(word)
                else:
                    return False
        return True
        