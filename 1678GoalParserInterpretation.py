# Leetcode 1678: Goal Parser Interpretation (easy)
# string

class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        new = "" # the new string to be returned

        for i, c in enumerate(command):
            # G case
            if c == "G":
                new += "G"
            if c == "(":
                # o case
                if i < len(command): # to avoid out of range exception
                    # if next character is a bracket
                    if command[i+1] == ")": 
                        new += "o"
                # al case
                if i < len(command) - 3: # to avoid out of range exception 
                    # if next 3 characters form "al)"
                    if command[i+1] == "a" and command[i+2] == "l" and command[i+3] == ")":
                        new += "al"

        return new

# test cases   
solution = Solution()
command = "G()()()()(al)"
print(solution.interpret(command))
command = "(al)G(al)()()G"
print(solution.interpret(command))