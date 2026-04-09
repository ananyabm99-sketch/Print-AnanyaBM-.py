class Solution:
    def makeGood(self, s: str) -> str:
        st = []
        for i in s:
            if len(st)>0:
                if i==s[-1]:
                    st.append(i)
                elif i.upper()==st[-1] or i.lower()==st[-1]:
                    st.pop()
                else:
                    st.append(i)
            else:
                st.append(i)
        return "".join(st)
            
s = Solution()  
print(s.makeGood("Pp"))