class Solution:
    def isPowerOfTwo(self,n):
        if n <=0 :
            return False
        while n % 2==0:
            n=n//2
        return n==1
solution=Solution()
print(solution.isPowerOfTwo(3))
        
            
