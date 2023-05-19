# Leetcode 577: Reverse Words in a String (easy)
# string

# Given a string s, reverse the order of characters in each word within a sentence
# while still preserving whitespace and initial word order.

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        reversed = ""

        for word in s.split():
            reversed += word[::-1] + " "

        return reversed[:-1]
    
    
    # creative one-line solution: 
    # "Here I first reverse the order of the words and then reverse the entire string."
    def reverseWords2(self, s):
        return ' '.join(s.split()[::-1])[::-1]

# test cases
solution = Solution()
print(solution.reverseWords("Let's take LeetCode contest"))
print(solution.reverseWords2("God Ding"))
