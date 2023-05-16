# Leetcode 12: Int to Roman (medium)

class Solution:
    def intToRoman(self, num):
        romans = [
            ["I", 1],
            ["IV", 4],
            ["V", 5], 
            ["IX", 9],
            ["X", 10], 
            ["XL", 40],
            ["L", 50], 
            ["XC", 90],
            ["C", 100],
            ["CD", 400],
            ["D", 500],
            ["CM", 900],
            ["M", 1000]
            ]
        result = ""

        for sym, val in reversed(romans):
            if num // val:
                count = num // val
                result += (sym * count)
                num = num % val
        return result
    
solution = Solution()
print(solution.intToRoman(243))