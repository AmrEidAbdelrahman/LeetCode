class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        visited = []
        i = 0
        maxi = 0
        new = 0
        for i in range(0, len(s)):
            if s[i] not in visited:
                new += 1
                visited.append(s[i])
            else:
                if new > maxi:
                    maxi = new
                visited = visited[visited.index(s[i]) + 1:]
                visited.append(s[i])
                new = len(visited)
        if new > maxi:
            maxi = new
        return maxi 
        