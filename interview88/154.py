from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l1 = len(nums)
        left = -1
        right = l1 - 1

        while left <= right - 2:
            mid = (right - left) // 2 + left
            if nums[mid] < nums[right]:

                right = mid
            elif nums[mid] > nums[right]:
                left = mid
            else:
                right -= 1

        return nums[right]

if __name__ == '__main__':
    s1 = Solution()
    l1  = list(map(int,input().strip().split()))
    print(s1.findMin(l1))
