# Leetcode 2570. Merge Two 2D Arrays by Summing Values (easy)
# hashmap, array

class Solution(object):
    # O(n) beats 80%
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        id_val = {}

        for pair in nums1:
            id_val[pair[0]] = pair[1]

        for pair in nums2:
            if pair[0] not in id_val: id_val[pair[0]] = pair[1]
            else: id_val[pair[0]] += pair[1]

        for id in sorted(id_val):
            ans.append([id, id_val[id]])
        
        return ans

# test cases
solution = Solution()
nums1 = [[1,2],[2,3],[4,5]]
nums2 = [[1,4],[3,2],[4,1]]
print(solution.mergeArrays(nums1, nums2)) # [[1,6],[2,3],[3,2],[4,6]]
""" The resulting array contains the following:
- id = 1, the value of this id is 2 + 4 = 6.
- id = 2, the value of this id is 3.
- id = 3, the value of this id is 2.
- id = 4, the value of this id is 5 + 1 = 6. 
"""
nums1 = [[2,4],[3,6],[5,5]]
nums2 = [[1,3],[4,3]]
print(solution.mergeArrays(nums1, nums2)) # [[1,3],[2,4],[3,6],[4,3],[5,5]]
"""There are no common ids, so we just include each id with its value in the resulting list."""