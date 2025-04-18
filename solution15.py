class Solution(object):
    def mySqrt(self, x):
        result=0
        while (result+1)*(result+1)<=x:
            result+=1
        return result
solution=Solution()
print(solution.mySqrt(4))