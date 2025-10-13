from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result  = 0
        for x in nums:
            result ^= x
        #print(result)
        return result