class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        d = {}
        w = words[0]
        for i in w:
            for j in words:
                if i not in j:
                    break
            else:
                d[i]=[]
                for k in words:
                    d[i].append(k.count(i))
        s=""
        for i in d:
            m = min(d[i])
            s=s+(i*m)
        return list(s)
s = Solution()
print(s.commonChars(["bella","label","roller"]))