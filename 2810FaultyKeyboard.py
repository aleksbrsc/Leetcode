# Leetcode 2810. Faulty Keyboard (easy)
# string

class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""

        for letter in s:
            if letter == "i": ans = ans[::-1]
            else: ans += letter
        
        return ans
    
# test cases
solution = Solution()
s = "string"
print(solution.finalString(s)) # "rtsng"
s = "poiinter"
print(solution.finalString(s)) # "ponter"