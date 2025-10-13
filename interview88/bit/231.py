class Solution:
    def isPowerOfTwo2(self, n: int) -> bool:
        result = 0
        for i in range(33):
            #print((1<<i))
            #print(n &(1<<i))
            if n&(1<<i) :#n&(1<<i) == 1
                result += 1

            #print('\n')
        #print(result)
        if result == 1:
            return True
        else:
            return False
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0  #100000



if __name__ == '__main__':
    s1 = Solution()
    n = 4

    print(s1.isPowerOfTwo(n))