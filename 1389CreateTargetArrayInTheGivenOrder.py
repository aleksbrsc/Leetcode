# Leetcode 1389. Create Target Array in the Given Order (easy)
# array

class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        target = []
        i = 0

        while i < len(nums):
            target.insert(index[i], nums[i])
            i += 1
        
        return target
    
    # top solution I found, pretty much same.
    def createTargetArray(self, nums, index):
        arr=[]
        for n,i in zip(nums,index): 
            arr.insert(i,n)
        return arr

# test cases
solution = Solution()
nums = [0,1,2,3,4]
index = [0,1,2,2,1]
print(solution.createTargetArray(nums, index)) # [0,4,1,3,2]
nums = [1,2,3,4,0]
index = [0,1,2,3,0]
print(solution.createTargetArray(nums, index)) # [0,1,2,3,4]
nums = [1]
index = [0]
print(solution.createTargetArray(nums, index)) # [1]