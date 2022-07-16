class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        students.sort()
        seats.sort()
        print(students, seats)
        res = 0
        for i in range(0, len(students)):
            res += abs(students[i] - seats[i])    
        return res