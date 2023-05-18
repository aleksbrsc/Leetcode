# Leetcode 2114: Maximum number of words found in setence (easy, easiest)
# string

class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        word_counts = []

        for s in sentences:
            words = s.split() # list of all the words in the sentence, split is based on whitespace between chars
            count = 0
            for word in words:
                count += 1
            word_counts.append(count)

        # sort the list in descending order
        sorted_word_count = sorted(word_counts, reverse=True)

        return sorted_word_count[0] # return the first (highest) value of the sorted list

# test cases
solution = Solution()
print(solution.mostWordsFound(["blah blah blah", "blah blah"]))