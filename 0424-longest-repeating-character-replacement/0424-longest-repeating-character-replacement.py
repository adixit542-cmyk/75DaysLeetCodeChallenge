class Solution:
    def characterReplacement(self, s, k):
        left = 0
        max_len = 0
        freq = {}

        for right in range(len(s)):
            # Count current character
            freq[s[right]] = freq.get(s[right], 0) + 1

            # If replacements needed exceed k, shrink window
            while (right - left + 1) - max(freq.values()) > k:
                freq[s[left]] -= 1
                left += 1

            # Update max length
            max_len = max(max_len, right - left + 1)

        return max_len