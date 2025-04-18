class Solution(object):
    def removeElement(self,nums):
        if not nums:
            return 0
        k=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
               nums[k] = nums[i]
               k+=1
        return k
nums=[2,3,4,4]
k=Solution.removeElement(nums)
print(k,nums[:k])