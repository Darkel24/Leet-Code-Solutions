class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])

        if m == 1 or n == 1:
            if any(1 in row for row in obstacleGrid):
                return 0
            else:
                return 1

        L=[[0 for _ in range(n)] for _ in range(m)]
        
        temp_x=obstacleGrid[0]
        if temp_x[0] == 1:   
           return 0
        else:
            for t in range(0,n):
                if temp_x[t] == 0:
                    L[0][t]=1
                if temp_x[t] == 1:
                    for i in range (t,n):
                        L[0][t]=0
                    break
        
       
        temp_y=[]
        for i in range(1,m):
            temp_y.append(obstacleGrid[i][0])
        
        for t in range(0,m-1):
            if temp_y[t] == 0:
                L[t+1][0]=1
            elif temp_y[t] == 1:
                for i in range (t,m-1):
                    L[i+1][0]=0
                break
       # print(L)

        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==1:
                    L[i][j] =0
                elif obstacleGrid[i][j]==0:
                    L[i][j]= L[i][j-1]+L[i-1][j]
      # print(L)    
        return L[-1][-1]
