from bisect import bisect_right
from collections import defaultdict
from typing import List
from bisect import bisect_left, bisect_right

class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.d1 = defaultdict(list)
        for x in range(len(arr)):
            self.d1[arr[x]].append(x)
        # print(self.d1)
        arr.sort()
        # print(arr)

    def query(self, left: int, right: int, value: int) -> int:
        result = 0
        if value in self.d1:
            l1 = self.d1[value]
            # print(l1)
            index1 = bisect_right(l1, right)
            index2 = bisect_left(l1, left)

            # print(f'length {index1 - index2}, index1 { index1}, index2 {index2}' )
            result = index1 - index2

        return result


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)

if __name__ == '__main__':
            l1 = list(map(int, input().strip().split()))
            s1 = RangeFreqQuery(l1)
