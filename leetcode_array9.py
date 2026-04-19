class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        new = []
        
        
        for i in nums1:
            new.append(i)
        for j in nums2:
            new.append(j)
        s = sorted(new)
        print(s)
        if len(s)%2==0:
            return (s[len(s)//2]+s[len(s)//2-1])/2
        else:
            return s[len(s)//2]
s=Solution()
print(s.findMedianSortedArrays([1,2],[3,4]))