class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0

        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            max_water = max(max_water, width * current_height)

            # Move the pointer at the shorter line because
            # the shorter line limits the current container.
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water
