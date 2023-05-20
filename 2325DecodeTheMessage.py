# Leetcode 2325: Decode the Message (easy)
# sting

class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        decoded = ""
        substitution_table = {}
        ascii = 97 # starting at "a"

        for char in key:
            if char not in substitution_table and char != " ":
                substitution_table[char] = chr(ascii)
                ascii += 1

        for char in message:
            if char in substitution_table:
                decoded += substitution_table[char]
            else: 
                decoded += " "

        return decoded
    
# test cases
solution = Solution()
key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
# result = "this is a secret"
print(solution.decodeMessage(key, message))
    

