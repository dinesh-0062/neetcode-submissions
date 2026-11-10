class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        values = set(nums)
        longest = 0

        # Only start counting at values that have no predecessor.
        for value in values:
            if value - 1 not in values:
                current = value
                streak = 1

                while current + 1 in values:
                    current += 1
                    streak += 1

                longest = max(longest, streak)

        return longest


# Time Complexity: O(n) average, because each value is visited a
# constant number of times across all consecutive runs.
# Space Complexity: O(n) for the set.
