# Leetcode 944: Delete Columns to Make Sorted (easy)
# string

class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        count = 0
        
        for tuple in zip(*strs): 
            if list(tuple) != sorted(tuple): 
                count += 1
                
        return count

# test cases
solution = Solution()
print(solution.minDeletionSize(["cba","daf","ghi"])) # 1
print(solution.minDeletionSize(["a","b"])) # 0
print(solution.minDeletionSize(["zyx","wvu","tsr"])) # 3
print(solution.minDeletionSize(["rrjk","furt","guzm"])) # 2
print(solution.minDeletionSize(["aihdtcw","hqlcusg","ptxfoxq"])) # 3
