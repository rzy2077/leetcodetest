class Solution:
    def getSum(self, a: int, b: int) -> int:
        x = 0xffffffff
        a, b = a & x, b & x
        while b != 0:
            nextBit = (a & b) << 1 & x #判断当前是否还有有效进位
            a = a ^ b #计算当前无进位的情况
            b = nextBit
        return a if a <= 0x7fffffff else  ~(a ^ x)
    #10100 = 16 + 4 n=a⊕b
    #10001 = 16 + 1 c= a&b << 1
    #00101
    #10000 << 1
    #100000
    #不能直接相加因为 without using the operators + and -.
'''

作者：Krahets
链接：https://leetcode.cn/problems/sum-of-two-integers/solutions/2361989/371-liang-zheng-shu-zhi-he-wei-yun-suan-a7coc/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
if __name__ == '__main__':
    print(hex(1))  # = 0x1 补码
    print(hex(-1))  # = -0x1 负号 + 原码 （ Python 特色，Java 会直接输出补码）

    print(hex(1 & 0xffffffff))  # = 0x1 正数补码
    print(hex(-1 & 0xffffffff))  # = 0xffffffff 负数补码

    print(-1 & 0xffffffff)  # = 4294967295 （ Python 将其认为正数）
