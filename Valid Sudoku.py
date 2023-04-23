class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """        
        columns = [[row[id] for row in board] for id in range(len(board[0]))] # transposition
        for row, row2 in zip(board, columns):
            for num, num2 in zip(row, row2):
                if (num.isdigit() and row.count(num) != 1) or (num2.isdigit() and row2.count(num2) != 1): #checking for reps in rows and columns
                    return False

        ###### Division into 3x3 blocks
        temp_arr = []
        arr = [] 
        for num in range(0,9,3): # division matrix to 3 columns 3x9
            for col in board:
                temp_arr.append(col[num:num+3])
        for num in range(0,27,3): # division columns to 9 blocks 3x3
            arr.append(temp_arr[num:num+3])
        # temp_arr:     List[List[str, str, str]]
        # arr:          List[List[List[str, str, str]]]
        ######

        values_arr = [] # Counting the temp_arr
        for quad in arr:
            temp_arr = [] # Temp list for 1 of 9 3х3 blocks

            for row in quad: # conversion matrix 3x3 to 1x9
                temp_arr += row

            for value in temp_arr: # Counting the number of each digit in a 3x3 block
                if value.isdigit():
                    values_arr.append(temp_arr.count(value))

        if values_arr != []:
            if max(values_arr) > 1: # if max(values_arr) > 1 -> sudoku invalid
                return False

        return True
            
            
