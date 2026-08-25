class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result, sum = nums[0], 0
        for i in range(len(nums)):           
            if sum < 0:
                sum = 0
            sum += nums[i]                           
            result = max(result, sum)            
        return result
        