class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid  # bad version, search left side
            else:
                left = mid + 1  # good version, search right side
        return left
