# Leetcode 3. Longest Substring Without Repeating Characters (medium)
# string 

class Solution(object):
    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "": return 0
        if s == " ": return 1
        substrings = []
        substring = ""
        
        for letter in s:
            if letter not in substring: substring += letter
            else:
                substrings.append(len(substring))
                index = substring.index(letter)
                substring = substring[index + 1:]
                substring += letter

        substrings.append(len(substring))

        return max(substrings)

# test cases
solution = Solution()
s = "abcabcbb"
print(solution.lengthOfLongestSubstring(s)) # 3 -> "abc"
s = "bbbbb"
print(solution.lengthOfLongestSubstring(s)) # 1 -> "b"
s = "pwwkew"
print(solution.lengthOfLongestSubstring(s)) # 3 -> "wke"
s = ""
print(solution.lengthOfLongestSubstring(s)) # 0 -> ""
s = " "
print(solution.lengthOfLongestSubstring(s)) # 1 -> " "
s = "dvdf"
print(solution.lengthOfLongestSubstring(s)) # 3 -> "vdf"