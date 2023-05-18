# Leetcode 1773: Count Items Matching a Rule (easy)
# string

class Solution(object):
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        ruleMap = { "type" : 0, "color" : 1, "name" : 2} # mapping each ruleKey to its corresponding index
        ruleIndex = ruleMap[ruleKey]

        print(ruleIndex)

        for item in items:
            if item[ruleIndex] == ruleValue:
                count += 1

        return count

# test cases
solution = Solution()

items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "type"
ruleValue = "phone"
print(solution.countMatches(items, ruleKey, ruleValue))
