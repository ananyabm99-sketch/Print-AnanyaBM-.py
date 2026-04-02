class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        if len(set(s))!=len(set(t)):
            return False
        d={}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=t[i]
            else:
                if d[s[i]]!=t[i]:
                    return False
        return True
s = Solution()
print(s.isIsomorphic(s="egg",t="add"))