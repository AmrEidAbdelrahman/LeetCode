class Solution(object):
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        def calc_dis(q,p):
            return abs((p[0] - q[0])**2 + (p[1] - q[1])**2 ) ** 0.5
        answer = []
        for q in queries:
            curr = 0
            for p in points:
                if calc_dis(p,q) <= q[2]:
                    curr += 1
            answer.append(curr)
            
        return answer