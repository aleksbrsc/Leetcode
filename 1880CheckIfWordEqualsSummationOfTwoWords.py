# Leetcode 1880. Check if Word Equals Summation of Two Words (easy)
# array

class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        letter1, letter2, letter3 = "", "", ""

        for i in firstWord:
            letter1 += str(ord(i) - 97)

        for i in secondWord:
            letter2 += str(ord(i) - 97)

        for i in targetWord:
            letter3 += str(ord(i) - 97)

        return (int(letter1) + int(letter2)) == int(letter3)
    

# test cases
solution = Solution()
firstWord = "acb"
secondWord = "cba"
targetWord = "cdb"
print(solution.isSumEqual(firstWord, secondWord, targetWord)) # true
firstWord = "aaa"
secondWord = "a"
targetWord = "aab"
print(solution.isSumEqual(firstWord, secondWord, targetWord)) # false
firstWord = "aaa"
secondWord = "a"
targetWord = "aaaa"
print(solution.isSumEqual(firstWord, secondWord, targetWord)) # true
