#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 计算最大收益
# @param prices int整型一维数组 股票每一天的价格
# @return int整型
#
from typing import List


class Solution:
    def maxProfit(self , prices: List[int]) -> int:
        # write code here
        result = 0
        for  i in range(1,len(prices)):
            temp = prices[i] - prices[i - 1]  #在计算两天的情况下，如果连续上涨则直接减去中间的值保证了只有起始与结尾
            if temp > 0:
                result += temp
        return result
    def maxProfit(self, prices: List[int]) -> int:   #greedy
        len1 = len(prices)
        dp = [[0 for _ in range(len1)] for _ in range(2)]
        print(dp)
        dp[0][0] = 0
        dp[0][1] = - prices[0]
        for i in range(1, len1):
            dp[i][0] = max(dp[i - 1][0],  dp[i - 1][1] + prices[i]) #dp[i][0] 表示第 i 天交易完后手里没有股票的最大利润  dp[i - 1][1] + prices[i] 卖出
            dp[i][1] = max(dp[i - 1][1],  dp[i - 1][0] - prices[i]) #dp[i][1] 表示第 i 天交易完后手里持有一支股票的最大利润（i 从 0 开始） dp[i - 1][0] - prices[i] 保留当前股票， dp[i - 1][1]保留原先股票
        return  dp[len1 - 1][0]
