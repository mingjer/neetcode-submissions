class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        
        res = ["" for i in range(len(words))]

        for word in words:
            for i in range(len(word)):
                if i >= len(res):
                    return False
                else:
                    res[i] += word[i]
                
                

        return res == words