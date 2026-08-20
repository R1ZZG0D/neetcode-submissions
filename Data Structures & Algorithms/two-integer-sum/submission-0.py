class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = {}
        for i in range(len(nums)):
            find = target - nums[i]
            if find in dict_nums:
                return [dict_nums[find],i]
            dict_nums[nums[i]] = i 