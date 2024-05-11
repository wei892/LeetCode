class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
            
        option1 = nums[:len(nums)-1] # house 1 to n-1
        option2 = nums[1:] # house 2 to end

        #rob house function from previous
        def robHouse(arr):
            prev1 = 0
            prev2 = 0
            for x in arr:
                maxMoney = max(prev1, prev2 + x)
                prev2 = prev1
                prev1 = maxMoney
            
            return prev1
        
        return max(robHouse(option1), robHouse(option2))



