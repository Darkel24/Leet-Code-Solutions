class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l=[]
        def subs(idx,tmp,lst,n,l):
            if idx>n:
                l.append(lst[:])
                return 
            lst.append(tmp[idx])
            subs(idx+1,tmp,lst,n,l)
            lst.pop()
            subs(idx+1,tmp,lst,n,l)
            return 
        lst=[]
        l=[]
        n=len(nums)-1
        subs(0,nums,lst,n,l)
        return sorted(l)

       
