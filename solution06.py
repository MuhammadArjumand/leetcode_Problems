class Solution(object):
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]
solution=Solution()
print(solution.isPalindrome(616))
