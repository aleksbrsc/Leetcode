import timeit

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        reversed_str = ""

        for word in s.split():
            reversed_str += word[::-1] + " "

        return reversed_str[:-1]

solution = Solution()

# Test case 1
s1 = "Let's take LeetCode contest"
runtime1 = timeit.timeit(lambda: solution.reverseWords(s1), number=10000)
print(f"Runtime for reverseWords('{s1}'): {runtime1} seconds")

# Test case 2
s2 = "God Ding"
runtime2 = timeit.timeit(lambda: solution.reverseWords(s2), number=10000)
print(f"Runtime for reverseWords('{s2}'): {runtime2} seconds")
