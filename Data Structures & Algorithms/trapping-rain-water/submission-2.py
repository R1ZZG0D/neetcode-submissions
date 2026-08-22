class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        res = 0
        if len(height) == 0:
            return 0
        for i in range(len(height)):
            max_left, max_right = 0, 0
            for j in range(i):
                max_left =  max(max_left, height[j])
            for k in range(i+1, len(height)):
                max_right = max(max_right, height[k])
            tmp = min(max_left, max_right) - height[i]
            if tmp < 0:
                continue
            res = res + tmp
        return res
        '''
        result = 0
        if len(height) == 0:
            return 0
        l, r = 0, len(height) - 1
        max_left, max_right = height[l], height[r]
        while l < r:
            if max_left < max_right:
                l += 1
                max_left = max(max_left, height[l])
                result += max_left - height[l]
            else:
                r -= 1
                max_right = max(max_right, height[r])
                result += max_right - height[r]         
            
        return result

