# Leetcode 2574. Left and Right Sum Differences (easy)
# array

class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer, left_sum, right_sum = [], [], []
        l = 0
        r = len(nums) - 1

        left, right = 0, 0
        while l < len(nums):
            # left sum
            if l - 1 >= 0:
                left += nums[l - 1]
                left_sum.append(left)
            else: left_sum.append(0)
            # right sum
            if r + 1 < len(nums):
                right += nums[r + 1]
                right_sum.append(right)
            else: right_sum.append(0)
            r -= 1
            l += 1
        
        for i, n in enumerate(left_sum):
            answer.append(abs(n - right_sum[::-1][i]))
        return answer
        
    # less verbose solution I found
    def leftRightDifference2(self, nums):
        sumLeft, sumRight = 0, sum(nums) 

        for i, n in enumerate(nums):
            sumRight -= n
            nums[i] = abs(sumLeft - sumRight)
            sumLeft += n

        return nums

# test cases
solution = Solution()
print(solution.leftRightDifference([10,4,8,3])) # [15,1,11,22]
print(solution.leftRightDifference([1])) # [0]
# print(solution.leftRightDifference2([10,4,8,3])) # [15,1,11,22]
# print(solution.leftRightDifference2([1])) # [0]