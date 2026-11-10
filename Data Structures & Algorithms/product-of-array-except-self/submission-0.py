class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Store the product of all values to the left of each index.
        result = [1] * len(nums)
        prefix = 1

        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        # Multiply by the product of all values to the right.
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result


# Time Complexity: O(n)
# Space Complexity: O(1) auxiliary space (output array excluded).
