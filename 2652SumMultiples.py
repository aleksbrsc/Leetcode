# Leetcode 2652. Sum Multiples (easy)
# array

class Solution(object):
    def sumOfMultiples(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        count = 0

        while i < n + 1:
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                count += i
            i += 1

        return count
            
# test cases
solution = Solution()
print(solution.sumOfMultiples(7)) # 21
print(solution.sumOfMultiples(10)) # 40
print(solution.sumOfMultiples(9)) # 30