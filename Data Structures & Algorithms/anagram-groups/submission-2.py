class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)

        for word in strs:
            tmp = [0] * 26
            for c in word:
                tmp[ord(c) - ord('a')] += 1
            hashMap[tuple(tmp)].append(word)
        
        return hashMap.values()