# Leetcode 58: Length of Last Word (easy)
# string

# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len((s.strip().split(" "))[-1])
    
    # modified version of my own which apparently jumps from beating 5% -> 75%
    def lengthOfLastWord2(self, s):
        return len(s.strip().split()[-1])


# test cases
solution = Solution()
print(solution.lengthOfLastWord("Hello World"))
print(solution.lengthOfLastWord("   fly me   to   the moon  "))