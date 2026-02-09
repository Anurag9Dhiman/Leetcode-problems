class Solution:
    def canPartition(self, nums):
        total_sum = sum(nums)
        if total_sum % 2 == 0:
            return False
        
        target_sum = total_sumk // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for s in range(target, nums-1, -1):
                dp[s] = dp[s] or dp[s - num]

        return dp[target]