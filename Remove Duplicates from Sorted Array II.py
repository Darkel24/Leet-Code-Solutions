class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=list(set(nums))
        l={i:nums.count(i) for i in k}
        for i in k:
            if(l[i]>2):
                for j in range(l[i]-2):
                    nums.remove(i)
        return len(nums)
