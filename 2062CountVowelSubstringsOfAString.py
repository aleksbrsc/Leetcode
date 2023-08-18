# Leetcode 2062. Count Vowel Substrings of a String (easy)
# string

"""
A substring is a contiguous (non-empty) sequence of characters within a string.

A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and 
has all five vowels present in it.

Given a string word, return the number of vowel substrings in word."""

class Solution(object):
    # One pass, no sliding window, O(n) top solution
    def countVowelSubstrings(self, word):
        vowels = {'a', 'e', 'i', 'o', 'u'}

        ans, last_consonant = 0, -1
        last_seen_vowels = {v: -2 for v in vowels}
        for i, x in enumerate(word):
            if x not in vowels:
                last_consonant = i
            else:
                last_seen_vowels[x] = i
                ans += max(min(last_seen_vowels.values())-last_consonant, 0)
        return ans

    # inefficient first solution
    def countVowelSubstrings2(self, word):
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
        while i <= len(word) -5:
            test = word[i]
            for j in range(i + 1, len(word)):
                if word[j] not in vowels: break
                else: test += word[j]
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

word = "duuebuaeeeeeeuaoeiueaoui"
print(solution.countVowelSubstrings(word)) # 81
