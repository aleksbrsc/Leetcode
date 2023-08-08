# Leetcode 2496. Maximum Value of a String in an Array (easy)
# string, array

class Solution(object):
    def maximumValue(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        # letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
        #             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
                    
        letters = "abcdefghijklmnopqrstuvwxyz"
    
        counts = []

        for string in strs:
            contains_letters = False
            for char in string:
                if char in letters:
                    contains_letters = True
            if contains_letters == True:
                counts.append(len(string))
                continue
            counts.append(int(string))

        return max(counts)

            
# test cases
solution = Solution()
strs = ["alic3","bob","3","4","00000"]
print(solution.maximumValue(strs)) # 5
strs = ["1","01","001","0001"] 
print(solution.maximumValue(strs)) # 1