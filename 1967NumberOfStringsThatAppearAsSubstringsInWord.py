# Leetcode 1967: Number of Strings That Appear as Substrings in Word (easy)
# string

# Given an array of strings patterns and a string word, 
# return the number of strings in patterns that exist as a substring in word.
# A substring is a contiguous sequence of characters within a string.

class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        count = 0

        for pattern in patterns:
            if pattern in word:
                count += 1

        return count
            
        
# test cases
solution = Solution()
patterns = ["a","abc","bc","d"]
word = "abc"
print(solution.numOfStrings(patterns, word)) # expected output: 3
patterns = ["a","b","c"]
word = "aaaaabbbbb"
print(solution.numOfStrings(patterns, word)) # expected output: 2
patterns = ["a","a","a"]
word = "ab"
print(solution.numOfStrings(patterns, word)) # expected output: 3
