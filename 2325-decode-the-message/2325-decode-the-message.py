class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        dic = {' ': ' '}
        j = 97
        for i in range(0, len(key)):
            if key[i] in dic:
                continue
            else:
                dic[key[i]] = str(chr(j))
                j += 1
        res = ""
        for i in range(0, len(message)):
            res += dic[message[i]]
        
        return res
        