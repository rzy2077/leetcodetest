from typing import List


class Solution:
    def findMin2(self, nums: List[int]) -> int:
        nums.extend(nums)
        l1 = len(nums)
        right = -1
        for index in range(l1):
            if nums[index] == nums[0]:
                right = index

        result = nums[right]
        while right > 0:
            if nums[right - 1] < nums[right]:
                result = nums[right - 1]
                right -= 1
            else:
                break

        return result
    def findMin(self, nums: List[int]) -> int:
        l1 = len(nums)
        left = 0
        right = l1 - 1
        result = -1
        while left <= right:
            mid = (right - left)// 2 + left
            if nums[mid] <= nums[l1 - 1]:
                result = nums[mid]
                right = mid - 1
            else:
                left = mid + 1
        
        return result
if __name__ == '__main__':
    s1 = Solution()
    l1 = list(map(int, input().strip().split()))
    print(s1.findMin(l1))
