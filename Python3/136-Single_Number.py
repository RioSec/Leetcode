class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # First thought was to use the logic of checking for empty list that saves a lot of time 
        unique = 0

        # Initate a variable with 0 to reuse it for XOR operator! 
        if nums != []: # Check for empty list 

            for i in nums: # For iter in list 

                unique ^= i # Repeated num is XORd with i and if both values are same then false is returned!

            return unique
