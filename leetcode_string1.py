#-------------------------------------STRING-------------------------------
#1.index of first occurrence in a string
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

#2.length of last word in a string
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s)-1
        while s[i]==" ":
            i-=1
        c=0
        while s[i]!=" " and i>-1:
            c+=1
            i-=1
        return c    
