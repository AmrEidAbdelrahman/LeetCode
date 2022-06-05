class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x > 0:
            y = str(x)
            for i in range(0,len(y)/2):
                #print(y[i] , y[len(y)-(i+1)] )
                #print(i, len(y)-(i+1))
                if y[i] == y[len(y)-(i+1)] and i<=len(y)-(i+1):
                    continue
                else:
                    return False
            return True
        elif x == 0:
            return True
        else:
            return False
            
        