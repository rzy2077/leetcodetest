class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        result2 = set()
        result = []
        temp = []
        len1 = len(nums)

        def find(index):

            if index > len1 - 1:
                return
            if tuple(temp) not in result2 and len(temp) > 1:
                result2.add(tuple(temp))
                result.append(temp.copy())
            for i in range(index + 1, len1):
                if (len(temp) > 0 and temp[-1] <= nums[i]) or (len(temp) == 0):
                    temp.append(nums[i])
                    find(i)
                    temp.pop()

        find(-1)
        return result