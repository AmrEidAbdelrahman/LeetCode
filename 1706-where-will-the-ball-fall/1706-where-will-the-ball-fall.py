class Solution(object):
    def findBall(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        res = []
        for i in range(0, len(grid[0])):
            # print("######")
            flag = False
            pos = i
            for arr in grid:
                # print(pos)
                if arr[pos] == 1 and len(arr)-1 == pos:
                    flag = True
                    break
                if arr[pos] == -1 and pos == 0:
                    flag = True
                    break
                if ( arr[pos] == 1 and arr[pos+1] == -1 ) or ( arr[pos] == -1 and arr[pos-1] == 1 ):
                    flag = True
                    break
                if arr[pos] == 1:
                    pos += 1
                elif arr[pos] == -1:
                    pos -= 1
            # print(flag)
            if flag:
                res.append(-1)
            else:
                res.append(pos)
            
        # print(res)
        return res