# Leetcode 125: Valid Palindrome (easy)
# two pointers

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all 
# non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

import re

class Solution:
    def isPalindrome(self, s):
        s = s.replace(" ", "").lower()
        s = re.sub(r'[^a-zA-Z0-9]','', s) # regex removes all non-alphanumeric chars
        odd = len(s) % 2

        for i in range(0, (len(s)// 2) + odd):
            left = s[i]
            right = s[-1-i]
            if left != right: return False

        return True


solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama")) # True
print(solution.isPalindrome("race a car")) # False
print(solution.isPalindrome(" ")) # True
    