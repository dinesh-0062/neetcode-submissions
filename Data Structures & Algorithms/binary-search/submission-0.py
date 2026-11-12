"""
Problem: Binary Search (LeetCode 704)
Difficulty: Easy
Topic: Binary Search

Approach:
The input array is sorted in ascending order. Keep an inclusive search
interval [left, right]. At each step, inspect its middle element:
- If it equals target, return its index.
- If it is smaller, discard the left half including mid.
- If it is larger, discard the right half including mid.
If the interval becomes empty, the target is absent and we return -1.

Time Complexity: O(log n), because the search interval is halved each step.
Space Complexity: O(1), because the algorithm uses only a few variables.
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


if __name__ == "__main__":
    test_cases = [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
        ([5], 5, 0),
        ([5], -5, -1),
        ([], 1, -1),
        ([-10, -5, 0, 3, 8], -10, 0),
        ([1, 2, 3, 4, 5], 5, 4),
        ([1, 2, 3, 4, 5], 1, 0),
    ]

    solution = Solution()
    for nums, target, expected in test_cases:
        actual = solution.search(nums, target)
        assert actual == expected, (
            f"nums={nums}, target={target}, expected={expected}, got={actual}"
        )

    print(f"All {len(test_cases)} test cases passed.")
