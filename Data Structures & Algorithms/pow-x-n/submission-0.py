class Solution:
    def myPow(self, x: float, n: int) -> float:

        # divide and conquer, T = O(logn)
        def helper(x, n):
            if x == 0: return 0
            if n == 0: return 1
            
            res = helper(x, n // 2)
            res *= res
            return x * res if n % 2 else res
        
        res = helper(x, abs(n))
        return res if n >=0 else 1 / res

        # pow in python
        # return x ** n

        # brute forc, T = O(n)
        # base = x

        # for _ in range(1, abs(n)):
        #     base *= x
        
        # return base if n > 0 else 1 / base