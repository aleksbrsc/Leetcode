# Leetcode 71: Simplify Path (medium)
# stack, string

class Solution():
    def simplifyPath(self, path: str) -> str:
        stack = []
        current = ""
 
        # iterates through chars of path and "/" at end for triggering if statement for last dir at end of path
        for char in path + "/":
            if char == "/":
                if current == "..": # pops the last element of the stack if .. and adds nothing
                    if stack: stack.pop()
                elif current != "" and current != ".": # if current is non-empty and not a period (which removes current directory by not even adding it in the first place)
                    stack.append(current) # adds the directory to the stack
                current = "" # resets the current directory string
            else:
                current += char # adds character to the current directory string
        return "/" + "/".join(stack) # returns properly formatted stack starting with root slash and separated with slashes

# test cases
solution = Solution()
print(solution.simplifyPath("/list/.././.../ch$/../of/path"))