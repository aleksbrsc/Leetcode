# Leetcode 2696. Minimum String Length After Removing Substrings
# string, stack

"""
You are given a string s consisting only of uppercase English letters.
You can apply some operations to this string where, in one operation,

you can remove any occurrence of one of the substrings "AB" or "CD" from s.

Return the minimum possible length of the resulting string that you can obtain.

Note that the string concatenates after removing the substring and could produce new "AB" or "CD" substrings.
"""

class Solution(object):
    # faster, uses stack/pop
    def minLength(self, s):
        stack = []

        for char in s:
            if stack and stack[-1] + char in ("AB", "CD"):
                stack.pop()
            else:
                stack.append(char)

        return len(stack)
    
    # slow, good sc
    def minLength2(self, s):
        """
        :type s: str
        :rtype: int
        """
        while "AB" in s or "CD" in s:
            j = 0
            while j < len(s) - 1:
                if s[j] + s[j+1] == "AB" or s[j] + s[j+1] == "CD":
                    s = s[:j] + s[j + 2:]
                    j + 2
                else: j += 1
        return len(s)
        


# test cases
solution = Solution()
s = "ABFCACDB"
print(solution.minLength(s)) # 2
"""  Explanation: We can do the following operations:
- Remove the substring "ABFCACDB", so s = "FCACDB".
- Remove the substring "FCACDB", so s = "FCAB".
- Remove the substring "FCAB", so s = "FC".
So the resulting length of the string is 2.
It can be shown that it is the minimum length that we can obtain."""

s = "ACBBD"
print(solution.minLength(s)) # 5
"Explanation: We cannot do any operations on the string so the length remains the same."