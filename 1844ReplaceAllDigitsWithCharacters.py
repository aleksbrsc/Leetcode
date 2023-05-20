# Leetcode 1844: Replace All Digits With Characters (easy)
# string

class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        for i, char in enumerate(s):
            if i % 2 != 0:
                result += chr(ord(s[i - 1]) + int(s[i]))
            else:
                result += char
        
        return result

    def replaceDigits(self, s):
        a = list(s)
        for i in range(1, len(a), 2):
            a[i] = chr(ord(a[i - 1]) + int(a[i]))
        return ''.join(a)

# test cases
solution = Solution()
s = "a1c1e1"
print(solution.replaceDigits(s))