class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) < 3:
            return max(nums)
        
        for x in range(2, len(nums)):
            option1 = nums[x - 2]

            if x - 3 < 0:
                option2 = 0
            else:
                option2 = nums[x -3]
            
            nums[x] += max(option1, option2)
        
        return max(nums[-1], nums[-2])