# Leetcode 1450. Number of Students Doing Homework at a Given Time (easy)
# array

class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        ans = 0

        for i in range(len(startTime)):
            for t in range(startTime[i], endTime[i] + 1):
                if t == queryTime: ans += 1

        return ans
    
    # a top solution, faster.
    def busyStudent2(self, startTime, endTime, queryTime):
        count = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime  <=endTime[i]:
                count += 1
        return count

# test cases
solution = Solution()
startTime = [1,2,3]
endTime = [3,2,7]
queryTime = 4
print(solution.busyStudent(startTime, endTime, queryTime)) # 1
startTime = [4]
endTime = [4]
queryTime = 4
print(solution.busyStudent(startTime, endTime, queryTime)) # 1
startTime = [61,74,11,54]
endTime = [61,75,65,92]
queryTime = 75
print(solution.busyStudent(startTime, endTime, queryTime)) # 2