class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        # return address.replace('.', '[.]')
        i = 0
        while i < len(address):
            if address[i] == '.':
                address = address[0:i] + '[.]' + address[i+1:]
                i += 3
            i += 1
        return address