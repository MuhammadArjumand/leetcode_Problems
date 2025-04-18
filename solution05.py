class Solution(object):
    def theMaximumAchievableX(self, nums, t):
        def theMaximum(nums,t):
            return nums + 2 * t
        return theMaximum(nums,t)
solution=Solution()
print(solution.theMaximumAchievableX(4,1))