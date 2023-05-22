# Leetcode 2678: Number of Senior Citizens (easy)
# string

class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        count = 0

        for passenger in details:
            if int(passenger[-4] + passenger[-3]) > 60:
                count += 1
        
        return count

    # top one line solution
    def countSeniors(details: list[str]) -> int:
        return sum(int(detail[11:13]) > 60 for detail in details)

# test cases
solution = Solution()
details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
print(solution.countSeniors(details))