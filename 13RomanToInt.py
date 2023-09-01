# Leetcode 13: Roman to Integer (easy)
# hashmap, string

# convert the given roman numeral string into an integer value
#   (the idea is, if a numeral is lesser than the next numeral, 
#   subtract the lesser numeral from the total. Otherwise, add regularly)
#
#   e.g.  IX = 0 - 1 + 10 = 9
#   e.g.  IV = 0 - 1 + 5 = 4
#   e.g.  CXXI = 0 + 100 + 10 + 10 + 1
#   e.g.  MCMXIV = 0 + 1000 - 100 + 1000 + 10 - 1 + 5 = 1914
# 

class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        # hashmap mapping each roman numeral to its integer value
        romans = {  "I" : 1,
                    "V" : 5,
                    "X" : 10,
                    "L" : 50,
                    "C" : 100,
                    "D" : 500,
                    "M" : 1000, }

        for i in range(len(s)):
            # checks if next numeral exists to avoid indexing out of range error
            # and checks if the numeral is lesser than the next,
            if i + 1 < len(s) and romans[s[i]] < romans[s[i + 1]]:
                ans -= romans[s[i]] # if it is, subtract
            else: ans += romans[s[i]] # if it is not, add

        return ans  
        
# test cases
solution = Solution()
print(solution.romanToInt("IX")) # 9
print(solution.romanToInt("IV")) # 4
print(solution.romanToInt("CXXI")) # 121
print(solution.romanToInt("MCMXIV")) # 1914