class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # row = {}
        # for i in range(1, numRows+1):
        #     row[i] = []
        # if numRows == 1:
        #     return s
        # plus = (numRows * 2) - 2
        # for i in range(0,len(s)+plus, plus):
        #     print("LOOP ", i)
        #     if i < len(s):
        #         row[1].append(s[i]) 
        #     for k in range(2,numRows):
        #         if (i - k + 1) > 0 and (i + k - 1) <= len(s):
        #             row[k].append(s[i - k + 1])
        #         if (i + k - 1) < len(s):
        #             row[k].append(s[i + k - 1])
        #     if (i+numRows-1) < len(s):
        #         row[numRows].append(s[i+numRows-1])
        #     print(row)
        # res = ''
        # for i in range(1, numRows+1):
        #     res += ''.join(row[i])
        # return res
        if numRows == 1:
            return s
        row = {}
        forward = True
        for i in range(1, numRows+1):
            row[i] = []
        i = 0
        j = 1
        while i < len(s):
            row[j].append(s[i])
            if j%numRows == 0:
                forward = False
            if j%numRows == 1:
                forward = True
            j = j+1 if forward else j-1
            i += 1
        res = ''
        for i in range(0, numRows):
            res += ''.join(row[i+1])
        return res
        
'''
  
        0           6
        1       5   7
        2   4       8
        3           9
        
        A
        B   D
        C
        
        P           I           N
        A       L   S       I   G
        Y   A       H   R
        P           I
        
        |               |8
        |           |
        |       |
        |   |
        |
        
        |                   |
        |               |
        |           |
        |       |
        |   |
        |
'''