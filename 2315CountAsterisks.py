# Leetcode 2315: Count Asterisks (easy)
# string

class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        return sum(char.count('*') for i, char in enumerate(s.split('|')) if i % 2 == 0)
    
# test cases
solution = Solution()
a = "l|*e*et|c**o|*de|"
b = "iamprogrammer"
c = "yo|uar|e**|b|e***au|tifu|l"
print(solution.countAsterisks(a))
print(solution.countAsterisks(b))
print(solution.countAsterisks(c))
        