# Letcode 2716. Minimize String Length (easy)
# array, string, set

class Solution(object):
    # the only challenge here was not misinterpreting the description and sample cases
    # the final string will contain no duplicates
    def minimizedStringLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(set(s))
                     
# test cases
solution = Solution()
s = "aaabc"
print(solution.minimizedStringLength(s)) # 3
s = "cbbd"
print(solution.minimizedStringLength(s)) # 3
s = "dddaaa"
print(solution.minimizedStringLength(s)) # 2
s = "ipi"
print(solution.minimizedStringLength(s)) # 2
