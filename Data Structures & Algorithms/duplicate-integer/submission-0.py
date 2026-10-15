class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        previous=0

        for i in range(1,len(nums)):
            if nums[previous]==nums[i]:
                return True
            previous=previous+1

        
        return False
        