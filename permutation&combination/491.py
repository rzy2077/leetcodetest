class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []
        temp = []
        len1 = len(nums)

        def find(index):

            if index > len1 - 1:
                return
            if temp not in result and len(temp) > 1:
                result.append(temp.copy())
            for i in range(index + 1, len1):
                if (len(temp) > 0 and temp[-1] <= nums[i]) or (len(temp) == 0):
                    temp.append(nums[i])
                    find(i)
                    temp.pop()

        find(-1)
        return result


