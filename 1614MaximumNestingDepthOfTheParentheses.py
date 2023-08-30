# Leetcode 1614. Maximum Nesting Depth of the Parentheses (easy)
# stack

class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        ans, count = 0, 0

        for char in s:
            if char == "(":
                count += 1
                stack.append("(")
            if stack and char == ")":
                if count > ans: ans = count
                count -= 1
                stack.pop()
        
        return ans

# test cases
solution = Solution()
s = "(1+(2*3)+((8)/4))+1" 
print(solution.maxDepth(s)) # 3
s = "(1)+((2))+(((3)))"
print(solution.maxDepth(s)) # 3
