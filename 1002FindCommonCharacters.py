# Leetcode 1002. Find Common Characters (easy)
# string, array

class Solution(object):
    # inefficient first solution
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        common, sorted_words  = [], []

        for word in words:
            sorted_words.append(sorted(word))

        smallest = min(sorted_words)
        n = len(sorted_words)

        for letter in smallest:
            count = 0
            temp_sorted_words = [list(word) for word in sorted_words]  # Create copies
            for i in range(n):
                if letter in temp_sorted_words[i]:
                    count += 1
            if count == n:
                common.append(letter)
                for word in temp_sorted_words:
                    word.remove(letter)

        return common

# test cases
solution = Solution()
words = ["bella","label","roller"]
print(solution.commonChars(words)) # ["e","l","l"]
words = ["cool","lock","cook"]
print(solution.commonChars(words)) # ["c","o"]
words = ["bbddabab","cbcddbdd","bbcadcab","dabcacad","cddcacbc","ccbdbcba","cbddaccc","accdcdbb"]
print(solution.commonChars(words)) # ["b","d"]