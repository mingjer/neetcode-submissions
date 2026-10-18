class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        window = 0
        res = 0
        for n in nums:
            if n == 1:
                window += 1
                res = max(res, window)
            else:
                window = 0
        
        return res