from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS1(self, nums: List[int]) -> int:
        l1 = len(nums)
        visit = []
        maxLen = [0] * l1
        tempResult = []
        result = 0

        def find(index):
            if index == l1 - 1:
                return 1
            if maxLen[index] != 0:
                return maxLen[index]
            temp = 1
            for index2 in range(index + 1, l1):
                if nums[index] < nums[index2]:
                    temp = max(temp, find(index2) + 1)
            maxLen[index] = temp

            return maxLen[index]

        for i in range(l1):
            len1 = find(i)
            # print(maxLen)
            result = max(result, len1)
            # print(len1)
        return result

    def lengthOfLIS2(self, nums: List[int]) -> int:
        f = [0] * len(nums)
        for i, x in enumerate(nums):
            for j,y in enumerate(nums[:i]):
                if x > y:
                    f[i] = max(f[i], f[j])
            f[i] += 1
        return max(f)

    def lengthOfLIS(self, nums: List[int]) -> int:
        g = []
        for x in nums:
            j = bisect_left(g,x) #最接近 >= g[j]的
            if j == len(g): #找到的数字比当前小
                g.append(x)
            else:
                g[j] = x

        return len(g)

if __name__ == '__main__':
    s1 = Solution()
    a = input().split() #加了split是list不加是str
    a1 = list(map(int, a))
    #print(a1)
    #print(type(a1))
    print(s1.lengthOfLIS1(a1))