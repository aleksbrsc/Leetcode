# Leetcode 2278: Percentage of Letter in String (easy)
# string, math

class Solution(object):
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        count = 0

        for char in s:
            if char == letter:
                count += 1

        return (count * 100) // len(s)
    
    # one line solution (uses count)
    def percentageLetter2(self, s: str, letter: str) -> int:
        return (s.count(letter) * 100) // len(s)

# test cases    
solution = Solution()
s = "foobar"
letter = "o"
print(solution.percentageLetter(s, letter))
