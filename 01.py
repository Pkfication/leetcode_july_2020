class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        else:
            m = 1
            steps = 1
            for x in range(2,n):
                m += x
                if m <= n:
                    steps += 1 
                else:
                    break
        return steps
