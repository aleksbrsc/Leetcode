# Leetcode 1534. Count Good Triplets (easy)
# array

class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        ans, i, j, k = 0, 0, 0, 0

        while i < len(arr):
            while j < len(arr):
                while k < len(arr):
                    if i < j < k and abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        ans += 1
                    k += 1
                k = 0
                j += 1
            j = 0
            i += 1
            
        return ans
    
    # more condense solution... why do i increment an index instead of using range.
    def countGoodTriplets2(self, arr, a: int, b: int, c: int) -> int:
        co = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        co += 1
        return co

    # remaking
    def countGoodTriplets3(self, arr, a, b, c):
        ans = 0

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        ans += 1
        
        return ans
        

# test cases
solution = Solution()
arr = [3,0,1,1,9,7]
a = 7
b = 2
c = 3
print(solution.countGoodTriplets(arr, a, b, c)) # 4
arr = [1,1,2,2,3]
a = 0
b = 0
c = 1
print(solution.countGoodTriplets(arr, a, b, c)) # 0