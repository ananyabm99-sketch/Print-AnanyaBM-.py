

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        l =list(ransomNote)
        l1 = list(magazine)
        for i in range(len(l)):
            if l[i] in l1:
                l1.remove(l1[i])
            else:
                return False
        return True
s=Solution()
print(s.canConstruct("aab","baa"))

