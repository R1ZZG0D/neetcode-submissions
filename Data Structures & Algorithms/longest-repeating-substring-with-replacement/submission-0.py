class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        cnt = 0
        for i in range(len(s)):
            sub, freq = {}, 0
            for j in range(i, len(s)):
                sub[s[j]] = 1 + sub.get(s[j], 0)
                freq = max(freq, sub[s[j]])
                window = j - i + 1
                if window - freq <= k:
                    cnt = max(cnt, window)
        return cnt
        '''
        cnt, l = 0, 0
        sub = {}
        for r in range(len(s)):
            sub[s[r]] = 1 + sub.get(s[r], 0) #for the character at position r we increase its count by 1 and if it doesn't exist yet then it is set to a deafult value 0
            
            # if the window is not valid which means length of the window - count of max occurring character > k
            if ((r - l + 1) - max(sub.values())) > k:
                sub[s[l]] -= 1
                l += 1 
            cnt = max(cnt, r - l + 1)
        return cnt
            

