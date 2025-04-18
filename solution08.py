class Solution(object):
    def isValid(self,x):
        stacks=[]
        pairs={')':'(',']':'[','}':'{'}
        for char in x:
            if char in pairs:
                if not stacks or stacks.pop()!=pairs[char]:
                    return False
            else:
                stacks.append(char)
        return not stacks
solution=Solution()
print(solution.isValid('()'))
