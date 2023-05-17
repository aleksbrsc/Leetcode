# Leetcode 155: Min Stack
# stacks
# all functions must have a time complexity of O(1), meaning no sorting or iterating through list

class MinStack:
    
    def __init__(self):
        self.stack = [] # the regular stack
        self.min_stack = [] # stack for the minimum numbers, (this avoids needing to sort: if we ensure this stack is always in descending order, then the top of the stack will always have the minimum value to be retrieved by getMin with min_stack[-1] -> meaning time complexity O(1))

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        # if min stack empty or val is less than or equal to the current minimum value
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val) # append the new minimum value to the min stack

    def pop(self):
        """
        :rtype: None
        """
        if self.stack: # if stack not empty
            if self.stack[-1] == self.min_stack[-1]: # if top of both stack and min stack are the same value
                self.min_stack.pop() # then pop it from min stack as well
            self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if self.stack: # if stack not empty
            return self.stack[-1] # return top of the stack

    def getMin(self):
        if self.min_stack: # if min stack not empty
            return self.min_stack[-1] # return top of the min stack / minimum value

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()