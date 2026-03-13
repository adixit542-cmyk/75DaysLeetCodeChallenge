class Solution(object):
    def twoSum(self, nums, target):

        for a in range(len(nums)):
            for i in range(a+1, len(nums)):
                if target - nums[a] == nums[i]:
                    return [a, i]

        return None