#===============================================================

class Solution:
    def containsDuplicate(self, nums):
        num_set = set()
        
        for i in nums:
            if i in num_set:
                return True
            num_set.add(i)
            
        return False


s = Solution()
input_nums = [1, 2, 3, 4, 5, 9, 11, 7, 6]
result = s.containsDuplicate(input_nums)
print(result)
