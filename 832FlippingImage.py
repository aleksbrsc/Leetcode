# Leetcode 832. Flipping an Image (easy)
# array

class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []

        for row in image:
            temp = []
            for col in row:
                if col == 0:
                    temp.append(1)
                else: temp.append(0)
            ans.append(temp[::-1])
        
        return ans

# test cases
solution = Solution()
image = [[1,1,0],[1,0,1],[0,0,0]]
print(solution.flipAndInvertImage(image)) # [[1,0,0],[0,1,0],[1,1,1]]
image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
print(solution.flipAndInvertImage(image)) # [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]