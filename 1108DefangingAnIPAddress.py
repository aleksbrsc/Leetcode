# Leetcode 1108: Defanging an IP Address (easy, easiest)
# string

# given a valid IP address, return a defanged version of that IP address.
# a defanged IP address replaces every period "." with "[.]"

class Solution:
    def defangIPaddr(self, address):
        defanged = "" # the new defanged string

        for c in address: # for each character in the string
            if c == ".": # if the character is a period
                defanged += "[.]" # add this to defanged string instead
            else: defanged += c # if the character isnt a period add the character to the defanged string

        return defanged # return the defanged version of the ip address
    




















    
# test cases
solution = Solution()
print(solution.defangIPaddr("1.1.1.1"))