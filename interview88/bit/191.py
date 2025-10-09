class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        for x in range(32):
            if n & (1<<x):
                result += 1
        return result