class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        l = []
        x = []
        for i in s:
            if len(l)>0:
                if i=="#":
                    l.pop(-1)
                else:
                    l.append(i)
            else:
                if l!="#":
                    l.append(i)
        print(l)
        for j in t:
            if len(x)>0:
                if j=="#":
                    x.pop(-1)
                else:
                    x.append(j)
            else:
                if x!="#":
                    x.append(j)
        print(x)
        if str(l)==str(x):
            return True
        return False
            
s = Solution()
print(s.backspaceCompare("y#fo##f", "y#f#o##f"))