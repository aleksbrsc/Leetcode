# Leetcode 657: Robot Return to Origin (easy)
# string

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        horizontal = 0
        vertical = 0

        for move in moves:
            if move == "L":
                horizontal -= 1
            if move == "R":
                horizontal += 1
            if move == "D":
                vertical -= 1
            if move == "U":
                vertical += 1

        return horizontal == 0 and vertical == 0
    
    def judgeCircle2(self, moves):
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')

# test cases
solution = Solution()
print(solution.judgeCircle("UD"))
print(solution.judgeCircle("LRUD"))
print(solution.judgeCircle("LRUDD"))