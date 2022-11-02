class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        # letters = 'ACGT'
        # key = {}
        # key[start] = 0
        # level = 0
        # visited = set()
        # i = 0
        # print("$$", key.keys())
        # while len(key.keys()) > 0:
        #     print("#", key.keys()[0])
        #     curr = key.keys()[0]
        #     print("$$$", curr)
        #     # do mutation on nxt
        #     for i in range(0,8):
        #         print("##", i)
        #         for j in letters:
        #             word = curr[:i] + j + curr[i+1:]
        #             print("###", curr, " >> ",  word)
        #             print("####", bank)
        #             if word == end:
        #                 return key[curr] + 1
        #             if word in bank and word not in visited:
        #                 print("VALID: ", word)
        #                 key[word] = key[curr] + 1
        #     level = key[curr]
        #     key.pop(curr)
        #     visited.add(curr)
        # print(key, visited)
        # print(level)    
        queue = deque([(start, 0)])
        seen = {start}
        
        while queue:
            node, steps = queue.popleft()
            if node == end:
                return steps

            for c in "ACGT":
                for i in range(len(node)):
                    neighbor = node[:i] + c + node[i + 1:]
                    if neighbor not in seen and neighbor in bank:
                        queue.append((neighbor, steps + 1))
                        seen.add(neighbor)

        return -1