class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        triplets = []

        for i in range(len(nums) - 2):
            # Skip duplicate first values to avoid repeated triplets.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Since the array is sorted, no later triplet can sum to zero.
            if nums[i] > 0:
                break

            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip duplicate second and third values.
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return triplets
