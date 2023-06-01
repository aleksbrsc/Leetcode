# Leetcode 2037. Minimum Number of Moves to Seat Everyone (easy)
# array

class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        answer, i = 0, 0
        seats = sorted(seats)
        students = sorted(students)

        while i < len(seats):
            answer += abs(seats[i] - students[i])
            i += 1

        return answer

# test cases
solution = Solution()
seats = [3,1,5]
students = [2,7,4]
print(solution.minMovesToSeat(seats, students)) # 4 
seats = [4,1,5,9]
students = [1,3,2,6]
print(solution.minMovesToSeat(seats, students)) # 7
seats = [2,2,6,6]
students = [1,3,2,6]
print(solution.minMovesToSeat(seats, students)) # 4