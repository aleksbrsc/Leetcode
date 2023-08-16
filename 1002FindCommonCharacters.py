# Leetcode 1002. Find Common Characters (easy)
# string, array

class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        common = []

        # Count the frequency of characters in the first word
        char_count = {}
        for char in words[0]:
            char_count[char] = char_count.get(char, 0) + 1

        # Iterate through the rest of the words and update char_count
        for word in words[1:]:
            temp_count = {}
            for char in word:
                if char in char_count and char_count[char] > 0:
                    temp_count[char] = temp_count.get(char, 0) + 1
                    char_count[char] -= 1
            char_count = temp_count

        # Build the common characters list based on char_count
        for char, count in char_count.items():
            common.extend([char] * count)

        return common

# test cases
solution = Solution()
words = ["bella","label","roller"]
print(solution.commonChars(words)) # ["e","l","l"]
words = ["cool","lock","cook"]
print(solution.commonChars(words)) # ["c","o"]