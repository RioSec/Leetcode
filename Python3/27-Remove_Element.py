class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # Initialize index to 0, which represents the current position for the next non-target element
        index = 0

        # Iterate through each element of the input array using the i pointer
        for i in range(len(nums)):

            # For each element in nums[i], check if it is equal to the target value
            if nums[i] != val:

                # Set nums[index] to nums[i] to store the non-target element at the current index position
                nums[index] = nums[i]

                # Increment index by 1 to move the next position for the next non-target element
                index += 1

        # Finally, return the value of index
        return index

