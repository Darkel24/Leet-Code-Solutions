class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        M = [[0 for j in range(n)] for i in range(n)]
        if n == 1:
            return [[1]]
        a=0
        b=n-1
        r = 1
        while 2*r <= n:
            for i in range(r-1, n-r):
                a += 1
                b += 1
                M[r-1][i]=a
                M[i][n-r]=b
            a = b
            b = a + n -2*r+1
            for j in range(n-r,r-1,-1):
                a +=1
                b += 1
                M[n-r][j]=a
                M[j][r-1]=b
            r += 1
            a = b
            b = a + n -2*r+1
            
            #print(r)
        if 2*r == n+1:
            M[r-1][r-1]=b+1
        return M
        
