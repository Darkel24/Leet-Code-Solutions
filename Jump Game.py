class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        dp=[False for _ in range(n-1)]
        dp+=[True]
        for i in range(n-2,-1,-1):
            for j in range(i,min(n,i+nums[i]+1)):
                if dp[j]:
                    dp[i]=True
                    break
                #print(i,j,dp)
        return dp[0]
