class Solution:


    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)

        # Rotate the array using array slicing
        nums[:] = nums[-k:] + nums[:-k]
