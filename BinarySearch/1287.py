from bisect import bisect_right, bisect_left
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        l1 = len(arr)
        i = 0
        while i < l1:
            index = bisect_right(arr, arr[i])
            #print(index)
            #print(index - i)
            if (index - i)/ l1 > 1/4:
                return  arr[i]
            i = index
        return 0
    def findSpecialInteger2(self, arr: List[int]) -> int:
        l1 = len(arr)
        m = l1 // 4
        for i in (m, m* 2 -1):
            x = arr[i]
            if bisect_right(arr,x) - bisect_left(arr,x) > m:
                return x
        return arr[m * 3 + 2]
