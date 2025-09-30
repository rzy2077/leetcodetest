class Solution:
    def firstBadVersion(self, n: int) -> int:
        result = 0
        left = 0
        right = n
        while left <= right:
            mid = (right - left)//2 + left
            if isBadVersion(mid) == True: #You are given an API bool isBadVersion(version) which returns whether version is bad.
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result

if __name__ == '__main__':
        s1 = Solution()
        s2 = input().strip().split()

        print(s1.firstBadVersion(s2))