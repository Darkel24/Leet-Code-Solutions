class Solution:
    def countAndSay(self, n: int) -> str:
        dp = [ "" for i in range(0,n+1)]
        dp[1] = "1 "
        i = 2 ;
        while( i < n+1 ):
            print(f'i:{i} dp[{i-1}]:{dp[i-1]}')
            c = 0 
            for j in range(0,len(dp[i-1])-1):
                if( dp[i-1][j] == dp[i-1][j+1]):
                    c += 1;
                else:
                    dp[i] += chr(c+1+ord('0')) + dp[i-1][j] ;
                    c=0;
            dp[i] += ' ';
            i +=1
            

        return dp[-1][:-1];
