class Solution:
    def isAnagram(self, s, t):
        # An anagram must have the same length
        if len(s) != len(t):
            return False
        
        # Compare sorted characters
        return sorted(s) == sorted(t)