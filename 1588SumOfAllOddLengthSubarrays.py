# Leetcode 1588. Sum of All Odd Length Subarrays (easy)
# array

class Solution(object):
    # O(n^3) because of sum
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        odd_sum = 0

        for i in range(len(arr)):
            for j in range(i, len(arr), 2):
                odd_sum += sum(arr[i:j+1])
        
        return odd_sum
    
# test cases
solution = Solution()
print(solution.sumOddLengthSubarrays([1,4,2,5,3])) # 58
print(solution.sumOddLengthSubarrays([1,2])) # 3
print(solution.sumOddLengthSubarrays([10,11,12])) # 66