# Leetcode 2194: Cells in a Range on an Excel Sheet (easy)
# string

class Solution(object):
    # mistake is that columns and rows are the other way around in excel
    def cellsInRange(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        cells_in_range = [] # list of strings containing each cell in the range
        # alphabet list used for indexing
        alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
        'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 
        # split the pair of strings separated by a colon
        split_s = s.split(":") 

        # grab the values for each row/col start/end 
        starting_letter = split_s[0][0]
        ending_letter = split_s[1][0]
        starting_number = split_s[0][1]
        ending_number = split_s[1][1]

        # calculates the range of the rows and columns
        row_gap = alphabet.index(ending_letter) - alphabet.index(starting_letter)
        col_gap = int(ending_number) - int(starting_number)

        for row in range(row_gap + 1): # plus one because we need to include the last row in the iteration
            for col in range(col_gap + 1): # iterate through each column in the range of
                row_letter = alphabet[alphabet.index(starting_letter) + row] # sets the current row letter, my first submission used row_letter = alphabet[alphabet.index(ending_letter) - row_gap + row]
                column_number = int(starting_number) + col # sets the column number, increasing on iteration
                cells_in_range.append(row_letter + str(column_number)) # add the cell string to the list of cells

        return cells_in_range
    
    # popular one line leetcode solution
    def cellsInRangeOneLine(self, s: str) -> list[str]:
        return [chr(c) + chr(r) for c in range(ord(s[0]), ord(s[3]) + 1) for r in range(ord(s[1]), ord(s[4]) + 1)]

    # easier, faster solution
        # ord(character) gives ascii value of that character
        # chr(ascii) converts ascii value back to character

        # example:
        # ord("a")=97
        # chr(97)= a

        # ord("A")=65
        # chr(65)=A
    def cellsInRangeEasy(self, s):   
        first_row = int(s[1])
        last_row = int(s[4]) 
        cells=[] # list of cells in a range
       
        for char in range(ord(s[0]), ord(s[3])+1): # for each column letter in the range
            for i in range(first_row, last_row + 1): # for each row number in the range
                cells.append(chr(char)+str(i)) # add the column and row to the cells list as a cell string
        return cells # return the list of cell strings

# test cases
solution = Solution()
print(solution.cellsInRangeEasy("A2:E3"))
print(solution.cellsInRangeEasy("A1:B2"))
print(solution.cellsInRangeEasy("U7:X9"))