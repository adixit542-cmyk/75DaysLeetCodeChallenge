from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count_map = defaultdict(int)
        count_map[0] = 1   # base case: sum = 0 occurs once
        prefix_sum = 0
        result = 0

        for num in nums:
            prefix_sum += num
            # check if there's a prefix_sum - k
            if (prefix_sum - k) in count_map:
                result += count_map[prefix_sum - k]
            # update map
            count_map[prefix_sum] += 1

        return result
