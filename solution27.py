class Solution(object):
    def containsDuplicate(self,nums):
        seen=set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
nums=[1,2,2,3,4,5,6,7]
solution=Solution()
print(solution.containsDuplicate(nums))