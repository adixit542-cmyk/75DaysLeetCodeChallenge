from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        ans = right

        while left <= right:
            mid = (left + right) // 2
            hours = sum(math.ceil(pile / mid) for pile in piles)

            if hours <= h:
                ans = mid
                right = mid - 1  # try smaller speed
            else:
                left = mid + 1  # need faster speed

        return ans
    