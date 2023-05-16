# Leetcoded 20: Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = { ")" : "(",
                        "]" : "[",
                        "}" : "{"} 
        for char in s:
            if char in close_to_open:
                if stack and stack[-1] == close_to_open[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False

solution = Solution()
print(solution.isValid("([][[({})]])"))
print(solution.isValid("[{]}]"))
print(solution.isValid("([][[({)"))
