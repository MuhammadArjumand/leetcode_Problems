class Solution(object):
    def romanIntoInt(self,x):
        roman_integers={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        total=0
        prev_value=0
        for i in reversed(x):
            current_value=roman_integers[i]
            if current_value < prev_value:
                total-=current_value
            else:
                total+=current_value
            prev_value=current_value
        return total
solution=Solution()
print(solution.romanIntoInt("IX"))