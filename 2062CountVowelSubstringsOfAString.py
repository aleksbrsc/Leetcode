# Leetcode 2062. Count Vowel Substrings of a String (easy)
# string

"""
A substring is a contiguous (non-empty) sequence of characters within a string.

A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and 
has all five vowels present in it.

Given a string word, return the number of vowel substrings in word."""

class Solution(object):
    def countVowelSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        if len(word) == 5 and word.sort() != "aeiou":
            return 0

        substrings = []
        ans = 0
        vowels = ["a", "e", "i", "o", "u"]

        i = 0
        while i < len(word) -5:
            test = word[i]
            for j in range(i + 1, len(word)):
                if word[j] not in vowels: break
                else: test += word[j]
                print(test)
                if len(test) >= 5:
                    vowel_set = []
                    for letter in sorted(test):
                        vowel_set.append(letter)
                    if set(vowel_set) == set(vowels):
                        substrings.append(test)
                        ans += 1
            i += 1

        return ans

# test cases
solution = Solution()
word = "aeiouu"
print(solution.countVowelSubstrings(word)) # 2
"""
- "aeiou"
- "aeiouu"
"""

word = "unicornarihan"
print(solution.countVowelSubstrings(word)) # 0
# "Not all 5 vowels are present, so there are no vowel substrings."

word = "cuaieuouac"
print(solution.countVowelSubstrings(word)) # 7