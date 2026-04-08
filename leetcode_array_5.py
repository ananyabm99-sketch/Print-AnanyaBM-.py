from ast import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        l=""
        for i in range(m):
            l+=str(nums1[i])
        for j in range(n):
            l+=str(nums2[j])
        for i in range(len(l)):
            nums1[i]=int(l[i])
        nums1.sort()
s = Solution()      
s.merge([1,2,3,0,0,0],3,[2,5,6],3)  
