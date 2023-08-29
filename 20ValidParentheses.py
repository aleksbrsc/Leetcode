# Leetcoded 20: Valid Parentheses (easy)
# stack

class Solution(object):
    # revisit, faster submission?
    def isValid(self, s):
        stack = []
        closed_to_open = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }

        for bracket in s:
            if bracket not in closed_to_open:
                stack.append(bracket)
            else:
                if stack and closed_to_open[bracket] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return stack == []
    
    def isValid(self, s: str) -> bool:
        stack = []
        # hashmap mapping closed brackets to their corresp. open bracket 
        closed_to_open = { ")" : "(",
                        "]" : "[",
                        "}" : "{"} 
        for char in s: # iterate through each character in string
            if char in closed_to_open: # if its a closed bracket
                if stack and stack[-1] == closed_to_open[char]: # if the stack is not empty and its last item is a corresp. open bracket
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