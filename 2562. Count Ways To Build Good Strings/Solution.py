class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0] * (high+1)
        dp[0] = 1

        accum = 0
        for i in range(min(zero, one), high+1):
            if i >= zero:
                dp[i] += dp[i - zero]
            if i >= one:
                dp[i] += dp[i - one]
            if i >= low:
                accum += dp[i]

        # print(dp)
        return accum % (10**9 + 7)


