# Leetcode 1047. Remove All Adjacent Duplicates In String (easy)
# string, stack

class Solution(object):
    # faster using stack
    def removeDuplicates(self, s):
        stack, ans = [], ""

        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else: stack.append(char)

        for char in stack:
            ans += char
        
        return ans

    # works, but doesn't pass time limit (needs stack)
    def removeDuplicates2(self, s):
        """
        :type s: str
        :rtype: str
        """
        contains_duplicates = True

        while contains_duplicates:
            i = 0
            a = s
            while i < len(s) - 1: 
                if s[i] == s[i+1]: 
                    s = s[:i] + s[i + 2:]
                    i += 2
                else: i += 1
            if s == a: return s

# test cases
solution = Solution()
s = "abbaca"
print(solution.removeDuplicates(s)) # "ca"
s = "azxxzy"
print(solution.removeDuplicates(s)) # "ay"