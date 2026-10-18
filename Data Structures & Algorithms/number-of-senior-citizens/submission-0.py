class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0

        for ppl in details:
            if int(ppl[11: 13]) > 60:
                res += 1
        
        return res