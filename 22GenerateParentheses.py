# Leetcode 22: Generate Parentheses (medium)
# backtracking

class Solution(object):
    # neetcode solution
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        parentheses_stack = []

        def backtrack(openN, closedN):
            # finished case
            if openN == closedN == n:
                result.append("".join(parentheses_stack))
                return

            # less open parentheses than n case
            if openN < n:
                parentheses_stack.append("(")
                backtrack(openN + 1, closedN)
                parentheses_stack.pop()

            # less closed parentheses than open brackets case
            if closedN < openN:
                parentheses_stack.append(")")
                backtrack(openN, closedN + 1)
                parentheses_stack.pop()

        backtrack(0, 0)
        return result
    
# test cases
solution = Solution()
print(solution.generateParenthesis(3))
# print(solution.generateParenthesis(4))