from heapq import heapify
import heapq
from typing import List
#, nlargest
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param a int整型一维数组
# @param n int整型
# @param K int整型
# @return int整型
#
class Solution:
    def findKth(self , a: List[int], n: int, K: int) -> int:
        #heapify([-x for x in a])
        #print(a)
        a1 = heapq.nlargest(3,a)
        #a2 = heapq.nsmallest(3,a)
        #print(a2)
        print(a1)
        return a1[-1]
        # write code here

if __name__ == '__main__':
    s1 = Solution()
    s1.findKth( [1,3,5,2,2],5, 3)