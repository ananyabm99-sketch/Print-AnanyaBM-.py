class Solution:
    def buildArray(self, target: list[int], n: int) -> List[str]:
        st = []
        ans = []
        for i in range(1, n + 1):
            if i in target:
                st.append("Push")
                ans.append(i)
            
            elif i not in target:
                st.append("Push")
                st.append("Pop")
            if ans == target:
                return st
            
        return st
s=Solution()
print(s.buildArray([1,3],3))