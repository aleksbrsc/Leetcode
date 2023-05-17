# Leetcode 12: Int to Roman (medium)
# hashmap

class Solution:
    def intToRoman(self, num):
        # using a hashmap to map each combination of roman numerals to their integer values
        # contains the edge cases of subtraction e.g. IV, IX being 4, 9
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

        for sym, val in reversed(romans): # iterate through the hashmap in descending order
            if num // val: # if we can floor divide the number by the value of the current symbol (because that means the translated number will definitely contain the symbol)
                count = num // val # figure out how many times the symbol will be used 
                result += (sym * count) # add to the result the symbol times the amountat of times its used
                num = num % val # remove the digit that was added to the result (basically, cut off the leftmost digit so we can look at the next one)
        return result
    
# test cases    
solution = Solution()
print(solution.intToRoman(243))
print(solution.intToRoman(1223))