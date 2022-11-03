def is_palindrom(word):
        l = len(word)
        if l % 2 == 0:
            return word[0:l//2] == word[::-1][0:l//2]
        else:
            return word[0:l//2] == word[::-1][0:l//2]
class Solution(object):
    
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
#         visited = []
#         res = 0
#         i = 0
#         while i < len(words):
#             word = words[i]
#             if word not in visited and word[::-1] in words and words.index(word[::-1]) != i:
#                 if words[words.index(word[::-1])] == word:
#                     if words.count(word) > 2:
#                         res += (words.count(word) - 2) * 2
#                 # print(word, word[::-1])
#                 visited.append(word)
#                 visited.append(word[::-1])
#                 res += len(word) * 2
#             i += 1    
#         j = 0
#         flag = False
#         for word in words:
#             if is_palindrom(word):
#                 flag = True
                
#         if flag:
#             res += 2
#         return res
        # a count variable contains the number of occurrences of each word
        count = Counter(words)
        answer = 0
        central = False
        for word, count_of_the_word in count.items():
            # if the word is a palindrome
            if word[0] == word[1]:
                if count_of_the_word % 2 == 0:
                    answer += count_of_the_word
                else:
                    answer += count_of_the_word - 1
                    central = True
            # consider a pair of non-palindrome words,
            # such that one is the reverse of another
            # word[1] + word[0] is the reversed word
            elif word[0] < word[1]:
                answer += 2 * min(count_of_the_word, count[word[1] + word[0]])
        if central:
            answer += 1
        return 2 * answer