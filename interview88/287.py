import sys
from typing import List
from collections import defaultdict
class Solution:
    def findDuplicateFalseVersion(self, nums: List[int]) -> int:
        #You must solve the problem without modifying the array nums(sort array) and using only constant extra space.
        l1 = len(nums)
        d1 = defaultdict(int)
        result = -1
        for x in nums:
            d1[x] += 1
            if d1[x] > 1:
                return x

        return result
    def findDuplicate(self, nums: List[int]) -> int:
        #You must solve the problem without modifying the array nums(sort array) and using only constant extra space.
        l1 = len(nums)
        d1 = defaultdict(int)
        result = -1
        for x in nums:
            d1[x] += 1
            if d1[x] > 1:
                return x
  #  12 34
        return result
if __name__ == '__main__':
        s1 = Solution()
        s2 = list(map(int,sys.stdin.readline().strip().split()))
        s3 = [1,3,4,2,2]
        print(s1.findDuplicate(s3))
