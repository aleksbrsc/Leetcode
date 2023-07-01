# Leetcode 1207. Unique Number of Occurrences (easy)
# array

class Solution(object):
    # slow
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        occurences, temp = [], []

        for i in set(arr):
            occurences.append(arr.count(i))

        for o in occurences:
            if o not in temp: temp.append(o)
            else: return False
        
        return True
    
# test cases
solution = Solution()
arr = [1,2,2,1,1,3]
print(solution.uniqueOccurrences(arr)) # true
arr = [1,2]
print(solution.uniqueOccurrences(arr)) # false
arr = [-3,0,1,-3,1,1,1,-3,10,0]
print(solution.uniqueOccurrences(arr)) # true