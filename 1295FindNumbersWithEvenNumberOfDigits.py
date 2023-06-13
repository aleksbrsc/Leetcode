# Leetcode 1295. Find Numbers with Even Number of Digits (easy)
# array

class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        
        for n in nums: 
            digits = [int(i) for i in str(n)]
            if len(digits) % 2 == 0:
                ans += 1
        
        return ans

    # realized list comprehension above was unnecessary
    def findNumbers2(self, nums):
        ans = 0
        for n in nums:
            if len(str(n)) % 2 == 0: ans += 1
        return ans
            

# test cases
solution = Solution()
nums = [12,345,2,6,7896]
print(solution.findNumbers(nums)) # 2
nums = [555,901,482,1771]
print(solution.findNumbers(nums)) # 1