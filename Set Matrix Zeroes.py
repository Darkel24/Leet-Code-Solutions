class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        rowzero=False
        #creating a variable for storing the information about the rows and the colomns
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if(matrix[i][j]==0):
                    matrix[0][j]=0
                    #setting the corresponding colomn to zero
                    if(i>0):
                        matrix[i][0]=0
                        #setting the corresponding row to zero
                    else:
                        rowzero=True
                        #intializing to True
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if(matrix[0][j]==0 or matrix[i][0]==0):
                    matrix[i][j]=0
        if(matrix[0][0]==0):
            for i in range(len(matrix)):
                matrix[i][0]=0
        if rowzero:
            for c in range(len(matrix[0])):
                matrix[0][c]=0
