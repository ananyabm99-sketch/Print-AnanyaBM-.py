
    
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        d ={}
        for i in range(len(nums)):
            if nums[i] in d:
                if i-d[nums[i]]<=k:
                    return True
            d[nums[i]]=i
        return False
s = Solution()
print(s.containsNearbyDuplicate([1,0,1,1], 1))

                            

