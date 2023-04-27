class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        visited = {n for n in nums if n > 0 and n < 100_001}
        smallest = 1
        while smallest in visited:
            smallest += 1
        return smallest
