class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_word = ""
        for s in strs:
            encoded_word += str(len(s)) + "@" + s
        return encoded_word

    def decode(self, s: str) -> List[str]:
        decoded_word = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "@":
                j += 1
            length = int(s[i:j])
            #i = j + 1
            #j = i + length

            decoded_word.append(s[j+1:j+1+length])
            i = j+1+length
        return decoded_word
       


