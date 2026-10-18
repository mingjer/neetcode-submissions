class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hashSet = set()

        for i in range(len(nums)):
            if nums[i] in hashSet:
                return True
            hashSet.add(nums[i])
         
        return False