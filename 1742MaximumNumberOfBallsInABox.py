# Leetcode 1742. Maximum Number of Balls in a Box (easy)
# array, hashmap

from collections import defaultdict
class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        box_to_balls = defaultdict(int)

        for i in range(lowLimit, highLimit + 1):
            box = 0
            for digit in str(i):
                box += int(digit)
            box_to_balls[box] += 1
        
        return max(box_to_balls.values())

# test cases
solution = Solution()
print(solution.countBalls(1, 10)) # 2
print(solution.countBalls(5, 15)) # 2
