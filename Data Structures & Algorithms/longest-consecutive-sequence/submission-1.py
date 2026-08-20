class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       seen = set(nums)
       longest = 0
       for i in seen:
        if i - 1 not in seen:
            current = i
            cnt = 1
            while current + 1 in seen:
                cnt += 1
                current += 1
            longest = max(longest,cnt)
       return longest


