# Leetcode 344: Reverse String (easy)
# string

class Solution(object):
    # beats 66.89% time complexity
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1] # 's[:] =' instead of 's =' -> modifies s in-place, so if you print(s) outside the scope of the function, its going to be modified correctly. This is probably the reason why my previous solutions with slice notation didnt work. 
    
# test cases
solution = Solution()
s = ["h","e","l","l","o"]
print(solution.reverseString(s))