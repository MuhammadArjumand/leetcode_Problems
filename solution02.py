class Solution(object):
    def maximumCount(self, nums):
        neg_count = 0
        pos_count = 0
        for num in nums:
            if num < 0:
                neg_count += 1
            elif num > 0:
                pos_count += 1
        return max(neg_count, pos_count)
solution=Solution()
nums = [-2, -1, -1, 1, 2, 3]
print(solution.maximumCount(nums))
