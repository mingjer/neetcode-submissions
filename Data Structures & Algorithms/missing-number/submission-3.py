class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # sort the list, and then you can just check the idx and the val if they are the same.
        # nums.sort() # O(nlogn)

        # for idx, val in enumerate(nums):
        #     if idx != val:
        #         return val - 1
        
        # return len(nums)

        summ = 0
        for i in range(1, len(nums) + 1):
            summ += i

        return summ - sum(nums)
