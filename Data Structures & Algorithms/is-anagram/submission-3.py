class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        def count(n):
            char_count = {}
            for char in n:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
            return char_count
        
        return count(s) == count(t)
            
        