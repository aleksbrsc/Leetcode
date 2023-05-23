# Leetcode 1436: Destination City (easy)
# easy

class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        source = set()
        dest = set()

        for path in paths:
            source.add(path[0]) # first index is the source
            dest.add(path[1]) # second index is the destination

        # the final destination is the only one that was never a source anywhere
        # we can find this by subtracting the destination set by the source set

        return list(dest - source)[0] # cast to list because set is not subscriptable (you need to take the value to return just the single string, not a set with a string inside)
    
    # similar solution i found, but iterates twice through n twice so its slower
    def destCity2(self, paths):
        source=[]
        destination=[]
        for i in paths:
            
            source.append(i[0])
            
            destination.append(i[1])
        
        for i in destination:
            if i not in source:
                return i


# test cases
solution = Solution()
paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
print(solution.destCity(paths))
paths = [["pYyNGfBYbm","wxAscRuzOl"],["kzwEQHfwce","pYyNGfBYbm"]]
print(solution.destCity(paths))