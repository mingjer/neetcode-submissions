class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashSet = {}

        for idx, val in enumerate(nums):
            diff = target - val
            if diff in hashSet:
                return [hashSet[diff], idx]
            hashSet[val] = idx