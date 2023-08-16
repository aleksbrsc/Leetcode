# Leetcode 2042. Check if Numbers Are Ascending in a Sentence (easy)
# string, array

class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        numbers = []
        tokens = s.split(" ")

        for token in tokens:
            if token.isdigit():
                numbers.append(int(token)) 
            # try: numbers.append(int(token))
            # except: pass

        s = 0
        for num in numbers:
            if num <= s: return False
            s = num

        return True

# test cases
solution = Solution()
s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
print(solution.areNumbersAscending(s)) # true
s = "hello world 5 x 5"
print(solution.areNumbersAscending(s)) # false
s = "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"
print(solution.areNumbersAscending(s)) # false