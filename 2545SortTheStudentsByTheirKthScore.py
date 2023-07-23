# Leetcode 2545. Sort the Students by Their Kth Score (medium)
# array, matrix

class Solution(object):
    def sortTheStudents(self, score, k):
        """
        :type score: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        temp = []
        ans = []

        for i in score:
            temp.append(i[k])
        
        temp.sort(reverse=True)
        
        for n in temp:
            for i in score:
                if n == i[k]:
                    ans.append(i)
        
        return ans
                
        
# test cases
solution = Solution()
score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]]
k = 2
print(solution.sortTheStudents(score, k)) # [[7,5,11,2],[10,6,9,1],[4,8,3,15]]
score = [[3,4],[5,6]]
k = 0
print(solution.sortTheStudents(score, k)) # [[5,6],[3,4]]