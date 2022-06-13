class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        x = True
        if len(s)%2 != 0:
            return False
        for i in range(0, len(s)):
            if s[i] in ['(', '[', '{']:
                stack.append(s[i])
            if s[i] in [')', ']', '}']:
                try:
                    x = stack.pop()
                except:
                    return False
                if not (ord(s[i]) == ord(x)+1 or ord(s[i]) == ord(x)+2):
                    print(x)
                    return False
        if len(stack) > 0:
            return False
        return True