class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        i=word.index(ch)
        a=word[0:i+1]
        a=a[::-1]
        b=word[i+1:]
        return a+b
s = Solution()
print(s.reversePrefix("abcdefd", "d"))