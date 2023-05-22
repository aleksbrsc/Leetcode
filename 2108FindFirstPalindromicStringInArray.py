# Leetcode 2108: Find First Palindromic String in the Array (easy, easiest)
# string

class Solution(object):
    # funnily was identical to the top solution
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for word in words:
            if word == word[::-1]:
                return word
        
        return ""
    
    # top one line solution
    def firstPalindrome2(self, words):
        return next((word for word in words if word == word[::-1]), "")

# test case
solution = Solution()
words = ["abc","car","ada","racecar","cool"]
print(solution.firstPalindrome(words))