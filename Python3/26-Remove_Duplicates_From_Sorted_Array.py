class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # Initialize a point i at the beginning of the array
        i = 0

        # Iterate through the array starting from the second element (j = 1)
        for j in range(1, len(nums)):

            # If the current element j is different from the previous element i
            if nums[j] != nums[i]:

                # Increment i to move to the next unique element
                i += 1

                # Update the current position i with the unique element (nums[j])
                nums[i] = nums[j]

        # Return the length of the modified array (i + 1)
        return i + 1
