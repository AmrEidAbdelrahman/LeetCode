class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        minus = operations.count('--X') + operations.count('X--')
        plus = operations.count('++X') + operations.count('X++')
        return plus - minus
                
        