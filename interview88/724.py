from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l1 = len(nums)
        s1 = sum(nums)
        left = 0
        result = -1
        for i in range(l1):
            right = s1 - left - nums[i]
            #print(f'left {left}, right {right}')
            if right  == left :
                result = i
                break
            left += nums[i]
        return result

if __name__ == '__main__':
        s1 = Solution()
        s2 = list(map(int,input().strip().split()))

        print(s1.pivotIndex(s2))

