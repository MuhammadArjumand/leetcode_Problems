class Solution(object):
    def plusOne(self, digits):
        str_num="".join(map(str,digits))
        num=int(str_num)
        num+=1
        result=list(map(int,str(num)))
        return result
solution=Solution()
print(solution.plusOne([9,9,9]))
