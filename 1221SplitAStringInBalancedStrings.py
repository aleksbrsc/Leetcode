# Leetcode 1221: Split a String in Balanced Strings (easy)
# string

class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        max_count = 0 # maximum number of balanced strings you can obtain

        for c in s:
            if c == "L": count += 1
            if c == "R": count -= 1
            if count == 0: max_count += 1 # if s is balanced, it will return to 0 a max count amount of times, where the max count is the amount of balanced substrings of s
        
        return max_count
    
solution = Solution()
print(solution.balancedStringSplit("RRL"))
 