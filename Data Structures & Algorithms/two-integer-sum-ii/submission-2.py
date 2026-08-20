class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        l, r = 0, len(numbers) - 1
        while l < r:
            current = numbers[l] + numbers[r]
            if current > target:
                r -= 1
            elif current < target:
                l += 1
            else:
                return [l+1 , r+1]
        '''
        seen = {}
        for i in range(len(numbers)):
            find = target - numbers[i]
            if find in seen:
                return [seen[find], i+1]
            seen[numbers[i]] = i+1
