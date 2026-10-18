class Solution:
    def findLucky(self, arr: List[int]) -> int:

        hashMap = defaultdict(int)

        for i in range(len(arr)):
            hashMap[arr[i]] += 1

        hashMap = dict(sorted(hashMap.items(), reverse = True))

        for key, val in hashMap.items():
            if key == val:
                return key

        return -1 