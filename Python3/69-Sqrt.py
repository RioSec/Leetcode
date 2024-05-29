class Solution:
    def mySqrt(self, x: int) -> int:
        # Start by assuming b is equal to x
        b = x

        # Use the Newton-Raphson formula to improve the estimate iteratively
        while b * b > x:

            # Continue the iteration until (b \times b) is less than or equal to x, meaning that b is the largest integer whose square is less than or equal to x
            b = (b + x // b) // 2

        # After the loop, return b as the integer part of the square root
        return b
