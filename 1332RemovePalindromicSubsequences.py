# Leetcode 1332: Remove Palindromic Subsequences (easy)
# string

class Solution(object):
    def removePalindromeSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        
        if s == s[::-1]:
            return 1
        
        return 2
    
    # one line version of mine that I found.
    def removePalindromeSub2(self, s):
        return 2 - (s == s[::-1]) - (s == "")

# test cases
solution = Solution()
print(solution.removePalindromeSub("ababa"))
print(solution.removePalindromeSub("abba"))
print(solution.removePalindromeSub("aaab"))
