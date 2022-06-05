class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
        }
        res = 0
        flag = False
        i = 0
        while i < len(s)-1:
            print(i, s[i])
            if dic[s[i]] >= dic[s[i+1]]:
                res += dic[s[i]]
                print('1', res)
                flag = False
                i += 1
            elif dic[s[i]] < dic[s[i+1]]:
                res += dic[s[i+1]] - dic[s[i]]
                i += 2
                print('2', res ,i)
                flag = True
                
        if flag == False or len(s)-1 == i:
            res += dic[s[len(s)-1]]
        
        return res