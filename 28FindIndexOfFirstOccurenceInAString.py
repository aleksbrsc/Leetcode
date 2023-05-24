# Leetcode 28: Find the Index of the First Occurrence in a String (easy)
# string

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i, char in enumerate(haystack):
            j = 0
            counter = 0
            while j < len(needle):
                if char == needle[j]:
                    counter += 1
                    j += 1
            if counter == len(needle):
                return i
        return -1

# test cases
solution = Solution()
haystack = "sadbutsad"
needle = "sad"
print(solution.strStr(haystack, needle)) # 0
haystack = "leetcode"
needle = "leeto"
print(solution.strStr(haystack, needle)) # -1