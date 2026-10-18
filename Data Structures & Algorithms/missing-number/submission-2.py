class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        nums.sort() # O(nlogn)

        for idx, val in enumerate(nums):
            if idx != val:
                return val - 1
        
        return len(nums)