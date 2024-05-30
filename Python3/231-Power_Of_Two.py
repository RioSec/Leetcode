class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Set x to 1
        x = 1

        # While x is x is less than n, multiple x by two
        while x < n:
            x *= 2

        # Once x isn't larger than n, set x to n    
        return x == n
