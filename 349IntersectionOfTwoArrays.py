# Leetcode 349. Intersection of Two Arrays (easy)
# array, hashmap

class Solution(object):
    # 80% tc
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        nums1, nums2 = set(nums1), set(nums2)
        for num in nums1:
            if num in nums2:
                ans.append(num)
        return ans

# test cases
solution = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
print(solution.intersection(nums1,nums2)) # [2]
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(solution.intersection(nums1,nums2)) # [9,4]
