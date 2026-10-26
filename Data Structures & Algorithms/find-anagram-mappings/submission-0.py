class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # brute force, T = O(n ^ 2)
        # res = []
        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         if nums1[i] == nums2[j]:
        #             res.append(j)
        #             break
        
        # return res

        # two pass
        hashMap = defaultdict(int)

        for idx, val in enumerate(nums2):
            hashMap[val] = idx
        
        res = []
        for n in nums1:
            res.append(hashMap[n])

        return res