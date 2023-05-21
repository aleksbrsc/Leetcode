# Leetcode 1309: Decrypt String from Alphabet to Integer Mapping (easy)
# string

class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        i = 0 

        while i < len(s): # while the index is within s
            if i + 2 < len(s) and s[i + 2] == '#': # if i + 2 is in the range and a hashtag
                val = int(s[i] + s[i + 1]) # combine the current and next index into a string and cast to integer
                result += chr(val + 96) # add the alphabetical character corresponding to the value
                i += 3 # skip past the hashtag's index
            else:
                result += chr(int(s[i]) + 96) # there is no hashtag awaiting in i + 2, so you can add the alphabet 
                i += 1 # and increment the index

        return result
    
# test cases
solution = Solution()
print(solution.freqAlphabets("10#11#12")) # jkab
print(solution.freqAlphabets("1326#")) # acz