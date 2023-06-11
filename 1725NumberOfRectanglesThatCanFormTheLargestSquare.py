# Leetcode 1725. Number Of Rectangles That Can Form The Largest Square (easy)
# array

class Solution(object):
    # 5% TS
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        max_lens = []
        ans = 0

        for i in rectangles:
            max_lens.append(min(i))

        for i in max_lens:
            if i == max(max_lens):
                ans += 1
        
        return ans
    
    # 91% TS
    def countGoodRectangles2(self, rectangles):
        max_lens = []

        for i in rectangles:
            max_lens.append(min(i))

        return max_lens.count(max(max_lens))
    
    # less speed? its different every time
    def countGoodRectangles3(self, rectangles):
        max_lens = [min(rectangle) for rectangle in rectangles]

        return max_lens.count(max(max_lens))

# test cases
solution = Solution()
rectangles = [[5,8],[3,9],[5,12],[16,5]]
print(solution.countGoodRectangles(rectangles)) # 3
rectangles = [[2,3],[3,7],[4,3],[3,7]]
print(solution.countGoodRectangles(rectangles)) # 3
