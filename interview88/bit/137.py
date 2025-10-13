from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        two,one = 0, 0
        for x in nums:
            one =  (one ^ x) & ~two # 二进制处理+1 (one ^ x)，~two 判断是否还需要处理
            two = (two ^ x) & ~one
        return one
