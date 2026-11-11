"""
Problem: Daily Temperatures (LeetCode 739)
Difficulty: Medium
Topic: Monotonic Stack

Approach:
Keep a stack of indices for days whose next warmer day is unknown.
The stack's temperatures stay non-increasing. When today's temperature
is higher than the temperature at the top index, today's day resolves
that earlier day; the answer is the difference between their indices.
Any index left in the stack has no warmer day, so its answer remains 0.

Time Complexity: O(n) — every index is pushed once and popped at most once.
Space Complexity: O(n) — the answer array and monotonic stack can each
hold up to n elements.
"""


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0] * len(temperatures)
        stack = []  # Indices waiting for a warmer temperature.

        for day, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                previous_day = stack.pop()
                answer[previous_day] = day - previous_day

            stack.append(day)

        return answer


if __name__ == "__main__":
    test_cases = [
        (
            [73, 74, 75, 71, 69, 72, 76, 73],
            [1, 1, 4, 2, 1, 1, 0, 0],
        ),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
        ([30, 60, 90], [1, 1, 0]),
        ([90, 80, 70, 60], [0, 0, 0, 0]),
        ([70], [0]),
        ([70, 70, 71], [2, 1, 0]),
        ([], []),
    ]

    solution = Solution()
    for temperatures, expected in test_cases:
        actual = solution.dailyTemperatures(temperatures)
        assert actual == expected, (
            f"Input: {temperatures}, expected: {expected}, got: {actual}"
        )

    print(f"All {len(test_cases)} test cases passed.")
