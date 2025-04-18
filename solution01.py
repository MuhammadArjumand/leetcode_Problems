class Solution(object):
    def twoSum(self, values, target):
            hash_map={}
            for i,num in enumerate(values):
                compliment=target-num
                if compliment in hash_map:      
                    return [hash_map[compliment],i]
                hash_map[num]=i
            return[]
solution=Solution()
values=(2,7,11,15)
target=9
print(solution.twoSum(values,target))