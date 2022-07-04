class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        minus = operations.count('--X') + operations.count('X--')
        plus = operations.count('++X') + operations.count('X++')
        return plus - minus
#         res = 0
#         for op in operations:
#             if op == '--X' or op == 'X--':
#                 res -= 1
#             elif op == '++X' or op == 'X++':
#                 res += 1
#         return res
                
        