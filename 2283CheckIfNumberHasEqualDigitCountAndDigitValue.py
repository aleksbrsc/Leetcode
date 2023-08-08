# Leetcode 2283. Check if Number Has Equal Digit Count and Digit Value (easy)
# array, string

class Solution(object):
    def digitCount(self, num):
        """
        :type num: str
        :rtype: bool
        """
        for i in range(len(num)):
            if int(num[i]) != num.count(str(i)): return False
        
        return True

# test cases
solution = Solution()
print(solution.digitCount("1210")) # true
print(solution.digitCount("030")) # false