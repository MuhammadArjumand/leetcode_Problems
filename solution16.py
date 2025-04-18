class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n
        prev2,prev1=1,2
        for i in range(3,n+1):
            current_value=prev1+prev2
            prev2=prev1
            prev1=current_value
        return prev1
solution=Solution()
print(solution.climbStairs(9))

        