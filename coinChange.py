#https://leetcode.com/problems/coin-change/submissions/
# Runtime: 2627 ms, faster than 19.22% of Python3 online submissions for Coin Change.
#Memory Usage: 14.3 MB, less than 39.77% of Python3 online submissions for Coin Change.
import math
from typing import List
class Solution:
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[math.inf]*(amount+1)
        dp[0]=0
        for number in coins:
            if number<amount+1:
                dp[number]=1
        for x in range(1,amount+1):
            for valor in coins:
                if x+valor<amount+1:
                    dp[x+valor]=min(dp[x]+1,dp[x+valor])
        if dp[-1]==math.inf:
            return -1
        return dp[-1]