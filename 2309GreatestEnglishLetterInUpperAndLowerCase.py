# Leetcode 2309. Greatest English Letter in Upper and Lower Case (easy)
# array, string

"""
Given a string of English letters s, return the greatest English letter which occurs as both a lowercase
and uppercase letter in s. The returned letter should be in uppercase. 
If no such letter exists,return an empty string.
An letter is greater than another letter if it appears later in the English alphabet.
"""

class Solution(object):
    # 95% tc, 80% sc
    def greatestLetter(self, s):
        s = set(s)
        upper, lower = 90, 122

        for i in range(26):
            if chr(upper - i) in s and chr(lower - i) in s:
                return chr(upper - i)
        return ""

    # inefficient first solution
    def greatestLetter2(self, s):
        """
        :type s: str
        :rtype: str
        """
        scanned = []
        doubles = []

        for letter in s:
            if letter == letter.lower():
                if letter.upper() in scanned: doubles.append(letter.upper())
                else: scanned.append(letter)
            if letter == letter.upper():
                if letter.lower() in scanned: doubles.append(letter.upper())
                else: scanned.append(letter)
        
        if doubles == []: return ""

        highest = "A"
        for letter in doubles:
            if ord(letter) - 65 > ord(highest) - 65: highest = letter

        return highest
            
    def greatestLetter3(self, s):
        s = set(s)
        upper, lower = ord("Z"), ord("z")

        for i in range(26):
            if chr(upper - i) in s and chr(lower - i) in s:
                return chr(upper - i)
        return ""

# test cases
solution = Solution()
s = "lEeTcOdE"
print(solution.greatestLetter(s)) # "E"
s = "arRAzFif"
print(solution.greatestLetter(s)) # "R"
s = "AbCdEfGhIjK"
print(solution.greatestLetter(s)) # ""
s = "Aa"
print(solution.greatestLetter(s)) # "A"