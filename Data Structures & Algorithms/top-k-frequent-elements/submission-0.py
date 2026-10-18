class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Count how often each number appears.
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        # Bucket numbers by frequency; no frequency can exceed len(nums).
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, frequency in counts.items():
            buckets[frequency].append(num)

        # Collect from highest frequency downward until k numbers are found.
        result = []
        for frequency in range(len(buckets) - 1, 0, -1):
            for num in buckets[frequency]:
                result.append(num)
                if len(result) == k:
                    return result

        return result


# Time Complexity: O(n), where n is the length of nums.
# Space Complexity: O(n) for the frequency map and buckets.
