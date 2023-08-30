# Leetcode 2032. Two Out of Three (easy)
# array, set 

class Solution(object):
    # 80% tc
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int] apparently can be set as well
        """
        nums1, nums2, nums3 = set(nums1), set(nums2), set(nums3)
        ans = set()

        for n in nums1:
            if n in nums2 or n in nums3:
                ans.add(n)
        for n in nums2:
            if n in nums1 or n in nums3:
                ans.add(n)
        
        return ans

    # top sol, remember intersection from set theory
    def twoOutOfThree(self, nums1, nums2, nums3):
        ret = []

        ret += set(nums1).intersection(set(nums2))
        ret += set(nums1).intersection(set(nums3))
        ret += set(nums2).intersection(set(nums3))

        return set(ret)
        
# test cases
solution = Solution()
nums1 = [1,1,3,2]
nums2 = [2,3]
nums3 = [3]
print(solution.twoOutOfThree(nums1,nums2,nums3)) # [3,2]
nums1 = [3,1]
nums2 = [2,3]
nums3 = [1,2]
print(solution.twoOutOfThree(nums1,nums2,nums3)) # [2,3,1]
nums1 = [1,2,2]
nums2 = [4,3,3]
nums3 = [5]
print(solution.twoOutOfThree(nums1,nums2,nums3)) # []