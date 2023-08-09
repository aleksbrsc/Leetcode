# Leetcode 2124. Check if All A's Appears Before All B's (easy)
# array, string

class Solution(object):
    def checkString2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        print(s, sorted(s))
        if list(s) == sorted(s): return True
        # for char in s:
        #     if char == "b":
        #         for rest in range(len())
        return False

    # faster, without casting and sorted
    def checkString(self, s):
        flag = False

        for char in s:
            if flag == True and char == "a": return False
            if char == "b": flag = True

        return True

# test cases
solution = Solution()
s = "aaabbb"
print(solution.checkString(s)) # true
s = "abab"
print(solution.checkString(s)) # false
s = "bbb"
print(solution.checkString(s)) # true