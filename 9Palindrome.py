# Leetcode 9: Palindrome (easy)
# Given an integer x, return true if x is a palindrome, and false otherwise.

def extract_digits(number):
    extracted_digits = []
    for i in str(number):
        extracted_digits.append(i)
    return extracted_digits

class Solution:
    def isPalindrome(self, x: int) -> bool:
        digits = extract_digits(x)
        # below uses slice notation for reversing list, first : indicates inclusion of all elements in list,
        # second : specifies step value which determines direction and size of the steps taken whiles slicing
        # -1 as step value means the slice should iterate over the original list in reverse order
        # because it takes steps of size -1, and its sign is negative so it moves from the end to the start 
        reversed_digits = digits[::-1] 
        # other ways to reverse a list:
            # reversed_digits = list(reversed(digits))

        if digits == reversed_digits:
            return True
        else: 
            return False
        
    # Follow up, can you do it without converting an int to a string?
    # (supposedly at least a medium problem)
    def isPalindromeFollowUp(self, x: int) -> bool:
        # negative numbers are always false
        if x < 0: return False

        # finding the digits place
        div = 1
        while x >= 10 * div:
            div *= 10

        while x:
            right = x % 10
            left = x // div

            if left != right: return False
            x = (x % div) // 10
            div = div / 100
        return True

    # simpler follow up solution
    def isPalindromeSimpler(self, x: int) -> bool:
        if x < 0: return False

        c = x 
        b = 0 # backwards number
        while c:
            b = b * 10 + c % 10 # appends rightmost digit after multiplying by 10 to add it to ten's place
            c //= 10 # removes rightmost digit
        return b == x
    
    # the half revert solution suggested by leetcode, 
    # its basis is that you only need to look at half of the int
    def isPalindromeRevert(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        b = 0
        while x > b:
            b = b * 10 + x % 10
            x //= 10

        return x == b or x == b // 10

# test cases

solution = Solution()

# regular tests
print("\nregular")

print(solution.isPalindrome(123))
print(solution.isPalindrome(121))
print(solution.isPalindrome(-1))
print(solution.isPalindrome(1))

# follow up tests
print("\nfollow up")

print(solution.isPalindromeFollowUp(123))
print(solution.isPalindromeFollowUp(121))
print(solution.isPalindromeFollowUp(-1))
print(solution.isPalindromeFollowUp(1))

# simpler tests
print("\nsimpler")

print(solution.isPalindromeSimpler(123))
print(solution.isPalindromeSimpler(121))
print(solution.isPalindromeSimpler(-1))
print(solution.isPalindromeSimpler(1))

# revert tests
print("\nrevert")

print(solution.isPalindromeRevert(123))
print(solution.isPalindromeRevert(121))
print(solution.isPalindromeRevert(-1))
print(solution.isPalindromeRevert(1))