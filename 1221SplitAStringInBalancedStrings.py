# Leetcode 1221: Split a String in Balanced Strings (easy)
# string

class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        max_count = 0 # maximum number of balanced substrings of s

        for c in s:
            if c == "L":
                count += 1
            if c == "R":
                count -= 1
            # if count goes back to 0, this means a new substring was confirmed balanced and so the max count is incremented
            if count == 0:
                max_count += 1

        return max_count
    
solution = Solution()
print(solution.balancedStringSplit("RRLLRLLR"))
 