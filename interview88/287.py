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
        #对有序数组进行二分，有序数组为n出现的次数
        result = -1
        l1 = len(nums)
        left = 0
        right = l1 - 1
        while left <= right:
            mid = (right - left)//2 + left
            count = 0
            for i in nums:
                if i <= mid:
                    count += 1
            if count <= mid :
                left = mid + 1
            else:
                right = mid - 1
                result = mid


        return result
if __name__ == '__main__':
        s1 = Solution()
        s2 = list(map(int,sys.stdin.readline().strip().split()))
        s3 = [1,3,4,2,2]
        print(s1.findDuplicate(s3))
