class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        # brute force T = O(n ^ 2), n = len(words)

        res = set()
        for i in range(len(words)):
            for j in range(len(words)):
                if len(words[i]) < len(words[j]) and words[i] in words[j]:
                    res.add(words[i])

        return list(res)