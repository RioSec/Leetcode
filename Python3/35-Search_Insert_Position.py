class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
 
        # Start by initializing two pointers (left and right) which represent the start and end indices of the search range within the list, nums.
        left, right = 0, len(nums) - 1

        # While loop that continues until the left pointer surpasses the right pointer
        while left <= right:

            # Within the loop, calculate mid with integer division (//) to confirm its an integer. The mid index is updated based on the current state of left and right
            mid = left + (right - left) // 2

            # At each iteration, check if the element at mid equals the target. If so, return the mid index as the position where target is found.
            if nums[mid] == target:
                return mid

            # If less than the target, it means the target should be inserted to the right of mid, so it updates the left pointer to mid + 1
            elif nums[mid] < target:
                left = mid + 1

            # If mid is greater than the target, it means the target should be inserted to the left of mid, so it updates the right pointer to mid - 1
            else:
                right = mid -1

        # If the loop exits without finding the target, it means there isn't a target present. If this happens, it means left represents the correct place where target should go to maintain the proper order. So left is returned.
        return left
