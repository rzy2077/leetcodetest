from typing import List
class Solution:

    def maximumCount(self, nums: List[int]) -> int:
        result = 0
        len1 = len(nums)
        left = 0
        right = len1 - 1

        leftPosition = 0
        rightPosition = 0
        while left <= right:
            mid = (right - left) // 2 + left

            if nums[mid] <= 0  :
                    if nums[mid] < 0 :
                        leftPosition = mid
                    left = mid + 1
            else:
                    rightPosition = mid
                    right = mid - 1
        print(f'leftPosition {leftPosition},rightPosition  {rightPosition}')
        return result



if __name__ == '__main__':
        s1 = Solution()
        #list1 = int(input().split(' '))
        list1 = list(map(int, input().split(' ')))
        print(list1)
        s1.maximumCount(list1)
