# Leetcode 496. Next Greater Element I (easy)
# array

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []

        for n in nums1:
            next = -1
            for j in range(nums2.index(n), len(nums2)):
                if nums2[j] > n: 
                    next = nums2[j]
                    break
            ans.append(next)

        return ans

# test cases
solution = Solution()
nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(solution.nextGreaterElement(nums1,nums2)) # [-1,3,-1]
nums1 = [2,4]
nums2 = [1,2,3,4]
print(solution.nextGreaterElement(nums1,nums2)) # [3,-1]