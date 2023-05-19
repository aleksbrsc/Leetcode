# Leetcode 1859: Sorting the Sentence (easy)
# string, sort
from collections import defaultdict

class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        sorted_map = defaultdict(list)
        sorted_sentence = ""

        for word in s.split():
            sorted_map[word[-1]] = word[:-1]

        sorted_map = dict(sorted(sorted_map.items()))

        for word in sorted_map.values():
            sorted_sentence += word + " "

        sorted_sentence = sorted_sentence[:-1]

        return sorted_sentence

# test cases
solution = Solution()
print(solution.sortSentence("is2 sentence4 This1 a3"))
print(solution.sortSentence("Myself2 Me1 I4 and3"))