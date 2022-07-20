class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        res = ""
        i = 0
        while i < len(command):
            if command[i] == 'G':
                res += 'G'
                i += 1
            elif command[i] == '(':
                if command[i+1] == 'a':
                    res += 'al'
                    i += 4
                else:
                    res += 'o'
                    i += 2
        return res
                    
                
        