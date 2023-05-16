# Leetcode 14: Longest Common Prefix (easy)

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        shortest_word_length = len(min(strs, key=len))
        current = []
        prefix = ""

        for index in range(shortest_word_length): # iterates through all the words
            current = []
            for word in strs:
                current.append(word[index])
                if len(current) == len(strs) and all(letter == current[0] for letter in current):
                    prefix += current[0]
                    current = []
        return prefix

strs = ["flow","flower","flight"]
solution = Solution()
print(solution.longestCommonPrefix(strs))