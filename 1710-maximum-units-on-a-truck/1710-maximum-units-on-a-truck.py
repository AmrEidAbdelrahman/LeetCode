class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        def get_box_with_max_unit(boxTypes):
            maxi = [0,0]
            for box in boxTypes:
                if box[1] > maxi[1]:
                    maxi = box
            if not maxi == [0,0]:
                boxTypes.remove(maxi)
            return maxi
        
        res = 0
        while truckSize > 0:
            curr = get_box_with_max_unit(boxTypes)
            if curr == [0,0]:
                return res
            if truckSize > curr[0]:
                truckSize -= curr[0]
                res += curr[0] * curr[1]
            else:
                res += curr[1] * truckSize
                truckSize = 0
        return res
        