# Leetcode 1769: Minimum Number of Operations to Move All Balls to Each Box (medium)
# string

class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        count = []

        for i, box in enumerate(boxes):
            min_ops = 0
            for j, n in enumerate(boxes):
                if j == i:
                    continue
                if n == "1":
                    min_ops += abs(i - j)
            count.append(min_ops)

        return count

    # top solution on leetcode beats 100% time space
    def minOperations2(self, boxes: str) -> list[int]:
        ans = [0]*len(boxes)
        leftCount, leftCost, rightCount, rightCost, n = 0, 0, 0, 0, len(boxes)
        for i in range(1, n):
            if boxes[i-1] == '1': leftCount += 1
            leftCost += leftCount # each step move to right, the cost increases by # of 1s on the left
            ans[i] = leftCost
        for i in range(n-2, -1, -1):
            if boxes[i+1] == '1': rightCount += 1
            rightCost += rightCount
            ans[i] += rightCost
        return ans

# test cases
solution = Solution()
print(solution.minOperations("110"))
print(solution.minOperations2("110"))
