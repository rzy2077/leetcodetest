#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 两次交易所能获得的最大收益
# @param prices int整型一维数组 股票每一天的价格
# @return int整型
#
from cmath import inf


class Solution:
    def maxProfit(self , prices: List[int]) -> int:
        k = 2
        # f[j][0]: 完成 j 次交易，手中无股票的最大利润
        # f[j][1]: 正在进行第 j 次交易，手中持有股票的最大利润
        # 大小为 (k+2) x 2。使用 k+2 是为了方便初始化，但实际只用到 j=1 到 j=k+1
        f = [[-inf] * 2 for _ in range(k + 2)]

        # 初始化： j=0 (0 次交易) 的利润是 0。
        # 这里用 j=1 到 k+1 来初始化 f[j][0] = 0 (表示在第0天，未买入股票时，利润为 0)
        for j in range(1, k + 2):
            f[j][0] = 0

        # 遍历每一天的价格 p
        for p in prices:
            # 倒序遍历交易次数 j，从 k+1 到 1
            for j in range(k + 1, 0, -1):
                # 状态 f[j][0] (第 j 次交易完成/卖出)
                f[j][0] = max(f[j][0], f[j][1] + p)

                # 状态 f[j][1] (第 j 次交易进行中/买入)
                # 注意：f[j-1][0] 必须是前一次交易完成的状态
                f[j][1] = max(f[j][1], f[j - 1][0] - p)

        # 最终返回完成 k 次交易且手中无股票的最大利润
        return f[k + 1][0]
