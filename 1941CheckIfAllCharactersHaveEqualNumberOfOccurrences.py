# Leetcode 1941: Check if All Characters Have Equal Number of Occurrences (easy)
# string

class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        occurences = {}

        for char in s:
            if char not in occurences:
                occurences[char] = 1
            else:
                occurences[char] = occurences[char] + 1

        values = sorted(occurences.values())
        return values[0] == values[-1]
    
# test cases
solution = Solution()
print(solution.areOccurrencesEqual("aabb"))