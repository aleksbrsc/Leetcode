# Leetcode 1704: Determine if String Halves Are Alike (easy)
# string

class Solution(object):
    # extremely simple but doesn't beat too many
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        half_length = len(s) // 2
        a = s[:half_length] # first half
        b = s[half_length:] # second half
        a_vowels = 0
        b_vowels = 0

        for char in a:
            if char in vowels:
                a_vowels += 1

        for char in b:
            if char in vowels:
                b_vowels += 1
    
        return a_vowels == b_vowels
    
    # leetcode top python solution
    # smarter approach with the middle, gets the count in one for loop only.
    def halvesAreAlike2(self, S: str) -> bool:
        vowels = "aeiouAEIOU" # interesting how we dont need a list if we're working with strings anyways
        mid, ans = len(S) // 2, 0
        for i in range(mid):
            if S[i] in vowels: ans += 1
            if S[mid+i] in vowels: ans -=1
        return ans == 0

# test cases
solution = Solution()
print(solution.halvesAreAlike("AbCdEfGh"))
print(solution.halvesAreAlike2("AbCdEfGh"))

