class Solution:
    def maxDepth(self, s: str) -> int:
        st = []
        m=0
        for i in s:
            if i in "[(":
                st.append(i)
                if len(st)>m:
                    m = len(st)

            elif i in ")]":
                st.pop()
        return m
            
s = Solution()
print(s.maxDepth("(1+(2*3)+((8)/4))+1"))