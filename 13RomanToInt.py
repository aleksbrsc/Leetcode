# Leetcode 13: Roman to Integer (easy)
# hashmap

class Solution:
    def romanToInt(self, s: str) -> int:
        # hashmap mapping each roman numeral to its integer value
        romans = {  "I" : 1,
                    "V" : 5, 
                    "X" : 10, 
                    "L" : 50, 
                    "C" : 100, 
                    "D" : 500, 
                    "M" : 1000 }
        
        result = 0

        for i in range(len(s)): # iterate length
            # first checks if there is a numeral after it to avoid string index out of range error
            # then checks if a greater numeral comes after a smaller numeral,
            # in which case the rule is that we subtract our result by the smaller number
            if i + 1 < len(s) and romans[s[i]] < romans[s[i + 1]]:
                result -= romans[s[i]] # subtract if smaller number
            else:
                result += romans[s[i]] # add if greater number

        return result
        
# test cases
solution = Solution()
print(solution.romanToInt("IX"))
print(solution.romanToInt("IV"))
print(solution.romanToInt("CXXI"))
print(solution.romanToInt("MCMXIV"))
