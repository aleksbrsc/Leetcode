# Leetcode 1678: Goal Parser Interpretation (easy)
# string

class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        new = ""

        for i, c in enumerate(command):
            if c == "G":
                new += "G"
            if c == "(":
                if i < len(command):
                    if command[i+1] == ")":
                        new += "o"
                if i < len(command) - 3:
                    if command[i+1] == "a" and command[i+2] == "l" and command[i+3] == ")":
                        new += "al"

        return new
    
solution = Solution()
command = "G()()()()(al)"
print(solution.interpret(command))
command = "(al)G(al)()()G"
print(solution.interpret(command))