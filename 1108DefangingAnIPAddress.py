# Leetcode 1108: Defanging an IP Address (easy)
# string

# given a valid IP address, return a defanged version of that IP address.
# a defanged IP address replaces every period "." with "[.]"

class Solution:
    def defangIPaddr(self, address):
        defanged = ""

        for i, c in enumerate(address):
            if c == ".":
                defanged += "[.]"
            else: defanged += c

        return defanged


solution = Solution()
print(solution.defangIPaddr("."))