class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # If mid element is greater than right element,
            # the minimum must be in the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # Otherwise, the minimum is in the left half (including mid)
                right = mid

        # At the end, left == right, pointing to the minimum
        return nums[left]
        