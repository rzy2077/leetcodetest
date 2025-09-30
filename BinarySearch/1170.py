from typing import List
from collections import defaultdict


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        # print(queries)
        result = []
        words2 = []
        queries2 = []
        for x in words:
            d1 = defaultdict(int)
            for y in x:
                d1[ord(y) - ord('a')] += 1

            list1 = list(d1.items())
            list1 = sorted(list1, key=lambda a: a[0])
            # 二重排序：先按 key 逆序，再按 value 升序
            # sorted_items = sorted(d1.items(), key=lambda kv: (-kv[0], kv[1]))
            # print(list1)
            words2.append(list1[0][1])
        for x in queries:
            d1 = defaultdict(int)
            for y in x:
                d1[ord(y) - ord('a')] += 1

            list1 = list(d1.items())
            list1 = sorted(list1, key=lambda a: a[0])
            # print(list1)
            queries2.append(list1[0][1])
        # print(queries2)
        words2.sort()
        # print(words2)
        l1 = len(words2)
        for x1 in queries2:
            #bisect1 = bisect_right(words2 , x1)
            #result.append(l1 - bisect1)
            left = 0
            right = l1 - 1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if words2[mid] > x1:

                    right = mid - 1

                else:
                    index = mid
                    left = mid + 1
            # 二重排序：先按 key 逆序，再按 value 升序
            #sorted_items = sorted(d1.items(), key=lambda kv: (-kv[0], kv[1]))
            #print(list1)
            # print(f'index {index}')
            result.append(l1 - 1 - index)

        return result


if __name__ == '__main__':
        s1 = Solution()
        s2 = input().strip().split()
        s3 = input().strip().split()
        print(s1.numSmallerByFrequency(s2,s3))