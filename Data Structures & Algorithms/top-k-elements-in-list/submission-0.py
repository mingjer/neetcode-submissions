class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]

        res = []

        hashMap = defaultdict(int)

        for n in nums:
            hashMap[n] += 1
        
        for key, val in hashMap.items():
            buckets[val].append(key)

        for i in range(len(buckets) - 1, -1, -1):
            res += buckets[i]
            if len(res) == k:
                return res
