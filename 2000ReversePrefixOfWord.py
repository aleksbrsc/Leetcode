# Leetcode 2000: Reverse Prefix of Word (easy)
# string

class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        result = ""
        found = False

        for n in word:
            result += n
            if n == ch and found == False:
                found = True
                result = result[::-1]

        return result

    # uses string's find method and is fastest
    def reversePrefix2(self, word, ch):
        idx = word.find(ch)    
        if idx:
            return word[:idx+1][::-1] + word[idx+1:]
        return word
        

# test case
solution = Solution()
word = "abcdefd"
ch = "d"
print(solution.reversePrefix(word, ch)) # "dcbaefd"
word = "xyxzxe"
ch = "z"
print(solution.reversePrefix(word, ch)) # "zxyxxe"
word = "abcd"
ch = "z"
print(solution.reversePrefix(word, ch)) # "abcd"