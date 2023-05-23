# Leetcode 2586: Count the Number of Vowel Strings in Range (easy)
# string

class Solution(object):
    def vowelStrings(self, words, left, right):
        """
        :type words: List[str]
        :type left: int
        :type right: int
        :rtype: int
        """
        vowels = "aeiou"
        i = left
        max = right
        vowel_strings = 0

        while i <= max:
            if words[i][0] in vowels and words[i][-1] in vowels:
                vowel_strings += 1
            i += 1

        return vowel_strings

# test cases
solution = Solution()
words = ["are","amy","u"]
left = 0
right = 2
print(solution.vowelStrings(words, left, right))