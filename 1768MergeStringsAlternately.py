# Leetcode 1768 Merge Strings Alternately (easy)
# string

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = "" # merged string to be returned

        # find the higher length of both words
        if len(word1) > len(word2):
            highest_length = len(word1)
        else: highest_length = len(word2)

        # for each index in the range of the highest length
        for i in range(highest_length):
            # add the current index character for word1 and then word2 to the merged string if they are within the range (to avoid string index out of range)
            if i < len(word1):
                merged += word1[i] 
            if i < len(word2):
                merged += word2[i]

        return merged # return the merged string
    
# test cases
solution = Solution()
word1 = "abc"
word2 = "pqr"
print(solution.mergeAlternately(word1, word2))
        

