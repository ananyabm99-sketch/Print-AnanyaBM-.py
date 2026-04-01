class Solution:
    def reverseVowels(self, s: str) -> str:
        l = []
        j=[]
        st= list(s)
        for i in range(len(s)):
            if s[i] in "aeiouAEIOU":
                l.append(s[i])
                j.append(i)  
        l = l[::-1]
        for i in range(len(l)):
            st[j[i]]=l[i]
        return "".join(st)