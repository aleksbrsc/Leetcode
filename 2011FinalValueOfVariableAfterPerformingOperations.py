# Leetcode 2011: Final Value of Variable After Performing Operations (easy, easiest)
# string

class Solution:
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        x = 0
        addition = ["++X", "X++"]
        subtraction = ["--X", "X--"]

        for o in operations:
            if o in addition:
                x += 1
            elif o in subtraction:
                x -= 1

        return x

# test cases
solution = Solution()
operations = ["--X","X++","X++"]
print(solution.finalValueAfterOperations(operations))