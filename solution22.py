class Solution(object):
    def isPalindrome(self,s):
        cleaned=''
        for char in s:
            if char.isalnum():
                cleaned += char.lower()
        return cleaned == cleaned[::-1]
a="A man, a plan, a canal: Panama"
solution=Solution()
print(solution.isPalindrome(a))


