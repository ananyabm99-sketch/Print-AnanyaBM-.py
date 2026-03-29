'''class Solution:
    def singleNumber(self,nums:list[int]):
        for i in nums:
            if nums.count(i)==1:
                return i
s = Solution()
print(s.singleNumber(nums=[1,2,2,3,3,4,4]))   #print(s.contain_duplicate(n=[1,2,3,4]))

class Solution:
    def singleNumber(self,nums:list[int]):
        sum = nums[0]
        for i in range(1,len(nums)):
            sum = sum^nums[i]
        return sum
s = Solution()
print(s.singleNumber(nums=[1,2,2,3,3,4,4]))

#majority elements in an array
class Solution:
    def singleNumber(self,nums:list[int]):
        s= set(nums)
        for i in s:
            if i in nums:
                if nums.count(i)>len(nums)//2:
                    return i
s = Solution()
print(s.singleNumber(nums=[1,2,2,3,3,3,3,3,3,3,4,4]))

class Solution:
    def singleNumber(self,nums:list[int]):
        s= sorted(nums)
        for i in range(len(nums)):
            return s[len(nums)//2]
s = Solution()
print(s.singleNumber(nums=[1,2,2,3,3,3,3,3,3,3,4,4]))

#Missing number in a list
class Solution:
    def missing_num(self,nums:list[int]):
        nums.sort()
        for i in range(0,len(nums)-1):
            if nums[i]+1!=nums[i+1]:
                return nums[i]+1
        else:
            if nums[0]!=0:
                return 0
            else:
                return len(nums)
        
su = Solution()
print(su.missing_num(nums=[1,2,3,4,5,7,8,9,10]))'''

class Solution:
    def missing_num(self,nums:list[int]):
        n = len(nums)+1
        s = (n*(n+1))//2
        total = sum(nums)
        return s-total
        
su = Solution()
print(su.missing_num(nums=[1,2,3,4,5,7,8,9,10]))

