class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        pre = strs[0]
        for w in strs[1:]:
            while not w.startswith(pre):
                pre = pre[:-1]
        return pre
s= Solution()   
print(s.longestCommonPrefix(["flower","flow","flight"]))