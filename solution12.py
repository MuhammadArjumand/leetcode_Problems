class Solution(object):
    def searchInsert(self,nums,target):
        for i,nums in enumerate(nums):
            if nums >= target:
                return i
        return len(nums)
solution=Solution()
print(solution.searchInsert([1, 3, 5, 6], 0))