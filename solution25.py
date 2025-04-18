class Solution(object):
    def isIsomorphic(self,s,t):
        map_s_to_t={}
        used_letter=set()
        for i in range(len(s)):
            char_s=s[i]
            char_t=t[i]
            if char_s in map_s_to_t:
                if map_s_to_t[char_s] != char_t:
                    return False
            else:
                if char_t in used_letter:
                    return False
                map_s_to_t[char_s]=char_t
                used_letter.add(char_t)
        return True
s="egg"
t="add"
solution=Solution()
print(solution.isIsomorphic(s,t))