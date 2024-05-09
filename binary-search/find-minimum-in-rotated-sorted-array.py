class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1
        result = max(nums)

        while left <= right:
            mid = (right + left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                result = min(nums[mid], result)
                right = mid - 1
        
        return result
        