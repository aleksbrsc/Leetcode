# Leetcoded 20: Valid Parentheses (easy)
# stack

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # hashmap mapping closed brackets to their corresp. open bracket 
        close_to_open = { ")" : "(",
                        "]" : "[",
                        "}" : "{"} 
        for char in s: # iterate through each character in string
            if char in close_to_open: # if its a closed bracket
                if stack and stack[-1] == close_to_open[char]: # if the stack is not empty and its last item is a corresp. open bracket
                    stack.pop() # removes last open bracket from the stack
                else:
                    return False # returns false if not in the stack or wrong bracket type
            else:
                stack.append(char) # add the character (bracket) to the stack
        return True if not stack else False # returns true if stack is empty, else false.

# test cases
solution = Solution()
print(solution.isValid("([][[({})]])"))
print(solution.isValid("[{]}]"))
print(solution.isValid("([][[({)"))
