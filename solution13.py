class Solution(object):
    def lengthOfLastWord(self, x):
        return len(x.strip().split()[-1])
solution=Solution()
print(solution.lengthOfLastWord("gg gangster"))
