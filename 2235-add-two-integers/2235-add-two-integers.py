class Solution(object):
    def sum(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        # neg = False
        # if num2 < 0:
        #     neg = True
        # for i in range(0, abs(num2)):
        #     num1 = num1 - 1 if neg else num1 + 1
        # return num1
        
        # return num1 + num2
        
        return num1.__add__(num2)