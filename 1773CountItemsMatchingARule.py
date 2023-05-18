# Leetcode 1773: Count Items Matching a Rule (easy)
# string

class Solution(object):
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0 # the number of items that match the given rule
        ruleMap = { "type" : 0, "color" : 1, "name" : 2} # mapping each ruleKey to its corresponding index
        ruleIndex = ruleMap[ruleKey] # the index of the rule key

        for item in items:
            if item[ruleIndex] == ruleValue: # if the item's rule key's value is equal to the rule value
                count += 1 # increment the count since the item matches the rule

        return count

# test cases
solution = Solution()
items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "type"
ruleValue = "phone"
print(solution.countMatches(items, ruleKey, ruleValue))
