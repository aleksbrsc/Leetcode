# Leetcode 1662: Check If Two String Arrays are Equivalent (easy)
# string

class Solution(object):
    # apparently beats 70% in both, but not much thought put into it at all
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        joined_word1, joined_word2 = "", ""

        for i in word1:
            joined_word1 += i

        for i in word2:
            joined_word2 += i
        
        return joined_word1 == joined_word2
    
    # one line solution
    # The join() method takes all items in an iterable and joins them into one string. 
    def arrayStringsAreEqualBetter(self, word1: list[str], word2: list[str]) -> bool:
        return ''.join(word1) == ''.join(word2)

# test cases
solution = Solution()
word1 = ["a", "cb"]
word2 = ["ab", "c"]
print(solution.arrayStringsAreEqual(word1, word2))
print(solution.arrayStringsAreEqualBetter(word1, word2))

        