class Solution(object):
    def strStr(self,haystack,needle):
        m,n=len(haystack),len(needle)
        if n==0:
            return 0
        for i in range(m-n+1):
            if haystack[i:i+n] == needle:
                return i
        return -1
haystack="sadbutsad"
needle="sad"
solution=Solution()
print(solution.strStr(haystack,needle))