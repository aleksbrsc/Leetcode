# Leetcode 2535. Difference Between Element Sum and Digit Sum of an Array (easy)
# array

class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        element_sum = 0
        digits = ""
        digits_sum = 0

        for n in nums:
            element_sum += n
            digits += str(n)

        for c in digits:
            digits_sum += int(c)

        return abs(element_sum - digits_sum)

# test cases
solution = Solution()
print(solution.differenceOfSum([1,15,6,3])) # 0 
print(solution.differenceOfSum([1,2,3,4])) # 9