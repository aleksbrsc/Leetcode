# Leetcode 2215. Find the Difference of Two Arrays (easy)
# hashmap, array

class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        ans = [[],[]]

        for n in nums1:
            if n not in nums2 and n not in ans[0]:
                ans[0].append(n)

        for n in nums2:
            if n not in nums1 and n not in ans[1]:
                ans[1].append(n)

        return ans

# test cases
solution = Solution()
nums1 = [1,2,3]
nums2 = [2,4,6]
print(solution.findDifference(nums1, nums2))