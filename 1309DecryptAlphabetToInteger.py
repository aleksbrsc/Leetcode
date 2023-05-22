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
            # case: 10# to 26#
            if i + 2 < len(s) and s[i + 2] == '#': # if is + 2 is in the range and a hashtag
                val = int(s[i] + s[i + 1]) # combine the current and next index into a string and cast to integer
                result += chr(val + 96) # add the alphabetical character corresponding to the value
                i += 3 # skip past the hashtag's index
            else: # case: 1 to 9
                result += chr(int(s[i]) + 96) # there is no hashtag awaiting in i + 2, so you can add the alphabet 
                i += 1 # and increment the index

        return result
    
    def freqAlphabets2(self, s):
        result = ""
        i = 0

        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == "#":
                val = int(s[i] + s[i + 1])
                result += chr(val + 96)
                i += 3
            else: 
                result += chr(int(s[i]) + 96)
                i += 1

        return result

    def freqAlphabets3(self, s):
        result = ""
        i = 0

        while i < len(s):
            if i + 1 < len(s) and s[i + 2] == "#":
                val = int(s[i] + s[i + 1])
                result += chr(val + 96)
                i += 3
            else:
                result += chr(int(s[i]) + 96)
                i += 1
        
        return result


    
# test cases
solution = Solution()
print(solution.freqAlphabets("10#11#12")) # jkab
print(solution.freqAlphabets2("1326#")) # acz
print(solution.freqAlphabets3("1326#")) # acz