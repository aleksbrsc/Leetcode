# Leetcode 412. Fizz Buzz (easy)
# array, str

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []

        for i in range(n):
            x = i + 1
            if x % 3 == 0 and x % 5 == 0:
                ans.append("FizzBuzz")
            elif x % 3 == 0:
                ans.append("Fizz")
            elif x % 5 == 0:
                ans.append("Buzz")
            else: ans.append(str(x))

        return ans
        
# test cases
solution = Solution()
n = 3
print(solution.fizzBuzz(n)) # ["1","2","Fizz"]
n = 5
print(solution.fizzBuzz(n)) # ["1","2","Fizz","4","Buzz"]
n = 15
print(solution.fizzBuzz(n)) # ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

