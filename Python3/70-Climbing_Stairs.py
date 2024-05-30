'''
The space-optimized solution further reduces the space complexity by using only two variables (prev and curr) instead of an entire DP table. It initializes prev and curr to 1 since there is only one way to reach the base cases (0 and 1 steps). Then, in each iteration, it updates prev and curr by shifting their values. curr becomes the sum of the previous two values, and prev stores the previous value of curr.
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        prev, curr = 1, 1
        for i in range(2, n+1):
            temp = curr
            curr = prev + curr
            prev = temp
        return curr

