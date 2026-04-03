'''class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l =[]
        j=1
        for i in range(len(nums)-1):
            if nums[0]+nums[-1]==target:
                l.append(0)
                l.append(len(nums)-1)
                break
            
            if nums[i]+nums[j]==target:
                l.append(i)
                l.append(j)
            j+=1
        return l
'''    
from ast import List


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        l =[]
        for i in range(len(nums)-1):
            for j in range(len(nums)):
                if i!=j:
                    if nums[i]+nums[j]==target:
                        l.append(i)
                        l.append(j)
                        return l
s= Solution()
print(s.twoSum([2,7,11,15],9))        
            
