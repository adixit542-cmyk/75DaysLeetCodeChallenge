class Solution:
    def findMaxAverage(self, nums, k):
        # Step 1: initial window sum
        window_sum = sum(nums[:k])
        max_sum = window_sum

        # Step 2: slide the window
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)

        # Step 3: return maximum average
        return max_sum / k