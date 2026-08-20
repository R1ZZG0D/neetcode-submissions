class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        result = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        return result
        '''
        result = [0] * len(nums)
        prod = 1
        cnt = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                prod *= nums[i]
            if nums[i] == 0:
                cnt += 1
        if cnt > 1:
                return result
        for i in range(len(nums)):            
            if cnt == 1 and nums[i] == 0:
                result[i] = prod
                return result
            elif cnt == 1 and nums[i] != 0:
                continue
            else:
                result[i] = prod // nums[i]
        return result

                
            


            


