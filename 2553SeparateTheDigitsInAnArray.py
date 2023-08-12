# Leetcode 2553. Separate the Digits in an Array (easy)
# array

class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp = ""
        ans = []

        for n in nums:
            temp += str(n)
        for c in temp:
            ans.append(int(c))
        
        return ans

    # other top solution
    def separateDigits2(self, nums):
        answer = []
        for item in nums:
            digit_list = list(map(int, str(item)))
            answer.extend(digit_list)
        return answer
    
# test cases
solution = Solution()
nums = [13,25,83,77]
print(solution.separateDigits(nums)) # [1,3,2,5,8,3,7,7]
nums = [7,1,3,9]
print(solution.separateDigits(nums)) # [7,1,3,9]

