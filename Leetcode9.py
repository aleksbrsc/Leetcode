# Leetcode 9: Palindrome (easy)
# Given an integer x, return true if x is a palindrome, and false otherwise.
def extract_digits(number):
    extracted_digits = []
    sign = "+"
    for i in str(number):
        extracted_digits.append(i)
    return extracted_digits

class Solution:
    def isPalindrome(self, x: int) -> bool:
        digits = extract_digits(x)
        reversed_digits = digits[::-1]

        if digits == reversed_digits:
            return True
        else: 
            return False
        
solution = Solution()
print(solution.isPalindrome(123))
print(solution.isPalindrome(121))
print(solution.isPalindrome(-1))
print(solution.isPalindrome(1))