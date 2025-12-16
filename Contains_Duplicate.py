from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # return len(nums) != len(set(nums))
        list_set = set()
        for n in nums:
            if n in list_set:
                return True
            list_set.add(n)
        return False
    

print(Solution().hasDuplicate([1,2,3]))