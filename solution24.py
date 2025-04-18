class Solution(object):
    def isHappy(self,n):
        seen=set()
        while 1!=n:
            if n in seen:
                return False
            seen.add(n)
            n=sum(int(digit)**2 for digit in str(n))
        return True
solution=Solution()
print(solution.isHappy(19))

