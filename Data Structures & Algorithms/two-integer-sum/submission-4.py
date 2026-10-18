class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = defaultdict(int)

        for idx, val in enumerate(nums):
            diff = target - val
            if diff in hashMap:
                return [min(hashMap[diff], idx), max(hashMap[diff], idx)]
            
            hashMap[val] = idx
        