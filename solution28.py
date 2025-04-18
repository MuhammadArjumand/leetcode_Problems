class Solution(object):
    def containsNearbyDuplicate(self,nums,k):
        seen=set()
        for i,num in enumerate(nums):
            if num in seen:
                return True
            seen.add(num)
            if len(seen) > k:
                seen.remove(nums[i-k])
        return False
nums=[1,0,1,1]
k=1
solution=Solution()
print(solution.containsNearbyDuplicate(nums,k))
