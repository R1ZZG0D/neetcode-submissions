class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        cnt = 0
        for i in range(len(s)):
            sub = set()
            for j in range(i, len(s)):
                if s[j] in sub:
                    break
                sub.add(s[j])
                cnt = max(cnt, len(sub))
        return cnt
        '''
        sub = set()
        l, cnt = 0, 0
        for r in range(len(s)):
            while s[r] in sub:
                sub.remove(s[l])
                l += 1
            sub.add(s[r])
            r += 1
            cnt = max(cnt, len(sub))
        return cnt
        



                






                
                
            
