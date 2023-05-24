# Leetcode 2351: First Letter to Appear Twice (easy)
# string

class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = ""

        for letter in s:
            if letter not in counter:
                counter += letter
            else:
                return letter

    # same thing but using set instead of string, useless though because even slower than string apparently      
    def repeatedCharacter2(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = set()

        for letter in s:
            if letter not in counter:
                counter.add(letter)
            else:
                return letter

# test cases
solution = Solution()
print(solution.repeatedCharacter("abb"))
print(solution.repeatedCharacter2("aba"))
