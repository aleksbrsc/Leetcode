# Leetcode 1876. Substrings of Size Three with Distinct Characters (easy)
# string, array

class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 3: return 0
        count = 0

        for i in range(len(s) - 2):
            if s[i] != s[i+1] and s[i] != s[i+2] and s[i+1] != s[i+2]: count += 1
        
        return count


        

# test cases
solution = Solution()
s = "xyzzaz"
print(solution.countGoodSubstrings(s)) # 1
s = "aababcabc"
print(solution.countGoodSubstrings(s)) # 4
s = ""
print(solution.countGoodSubstrings(s)) # 0
